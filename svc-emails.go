package emails

import (
	"context"
	"time"

	grpc_middleware "github.com/grpc-ecosystem/go-grpc-middleware"
	grpc_logrus "github.com/grpc-ecosystem/go-grpc-middleware/logging/logrus"
	grpc_opentracing "github.com/grpc-ecosystem/go-grpc-middleware/tracing/opentracing"
	grpc_prometheus "github.com/grpc-ecosystem/go-grpc-prometheus"
	opentracing "github.com/opentracing/opentracing-go"
	"github.com/sirupsen/logrus"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"

	lib "gitlab.com/SpoonQIR/Cloud/library/golang-common.git"
)

type EmailsService struct {
	Emailsconn *grpc.ClientConn
	Emailssvc  EmailsClient
	Emailsreco chan bool

	Id *lib.Identity
}

// InitEmails tst
func (s *EmailsService) InitEmails(emailsHost string, tracer opentracing.Tracer, logger *logrus.Logger) chan bool {
	logentry := logrus.NewEntry(logger)
	logopts := []grpc_logrus.Option{
		grpc_logrus.WithDurationField(func(duration time.Duration) (key string, value interface{}) {
			return "grpc.time_ns", duration.Nanoseconds()
		}),
	}

	otopts := []grpc_opentracing.Option{
		grpc_opentracing.WithTracer(tracer),
	}

	var err error

	connect := make(chan bool)

	go func(lconn chan bool) {
		for {
			logrus.Info("Wait for connect")
			r := <-lconn
			logrus.WithFields(logrus.Fields{"reconn": r}).Info("conn chan receive")
			if r {
				for i := 1; i < 5; i++ {
					s.Emailsconn, err = grpc.Dial(emailsHost,
						grpc.WithInsecure(),
						grpc.WithUnaryInterceptor(grpc_middleware.ChainUnaryClient(
							grpc_logrus.UnaryClientInterceptor(logentry, logopts...),
							grpc_opentracing.UnaryClientInterceptor(otopts...),
							grpc_prometheus.UnaryClientInterceptor,
						)),
						grpc.WithStreamInterceptor(grpc_middleware.ChainStreamClient(
							grpc_logrus.StreamClientInterceptor(logentry, logopts...),
							grpc_opentracing.StreamClientInterceptor(otopts...),
							grpc_prometheus.StreamClientInterceptor,
						)),
					)
					if err != nil {
						logger.Fatalf("did not connect: %v, try : %d - sleep 5s", err, i)
						time.Sleep(2 * time.Second)
					} else {
						s.Emailssvc = NewEmailsClient(s.Emailsconn)
						break
					}
				}
			} else {
				logrus.Info("end of goroutine - reconnect")
				return
			}
		}
	}(connect)

	logger.WithFields(logrus.Fields{"host": emailsHost}).Info("Connexion au service gRPC 'Emails'")

	//Identity
	s.Id = &lib.Identity{}
	go s.Id.Launch()

	connect <- true
	return connect
}

func (s *EmailsService) SendTemplate(ctx context.Context, usr *EmailTemplate) (*EmailTemplate, error) {
	for i := 0; i <= 5; i++ {
		md, ok := metadata.FromOutgoingContext(ctx)
		if !ok {
			logrus.Error("cannot get outgoing data")
		}
		logrus.WithFields(logrus.Fields{"usr": usr, "jwt": md.Get("authorization")}).Debug("send template")
		if usr == nil {
			logrus.Error("error send template, usr is nil")
		}
		if ctx == nil {
			logrus.Error("error send template, ctx is nil")
		}
		if md == nil {
			logrus.Error("error send template, md is nil")
		}
		if s.Emailssvc == nil {
			logrus.Error("error send template, s.Emailssvc is nil")
			s.Emailsreco <- true
		}
		grp, err := s.Emailssvc.SendTemplate(metadata.NewOutgoingContext(ctx, md), usr)
		logrus.WithFields(logrus.Fields{"ctx.err": ctx.Err(), "err": err}).Trace("error ctx get object")
		if err != nil {
			logrus.WithFields(logrus.Fields{"err": err}).Error("error send template")
			errStatus, _ := status.FromError(err)
			if errStatus.Code() == codes.Unavailable {
				s.Emailsreco <- true
			} else if errStatus.Code() == codes.Canceled {
				s.Emailsreco <- true
			} else if errStatus.Code() == codes.DeadlineExceeded {
				s.Emailsreco <- true
			} else if errStatus.Code() == codes.Aborted {
				s.Emailsreco <- true
			} else if errStatus.Code() == codes.Unauthenticated {
				logrus.WithFields(logrus.Fields{"jwt": md.Get("authorization")}).Info("ws-emails not identified")
				return nil, status.Error(codes.Unauthenticated, "unauthenticated")
			} else if errStatus.Code() == codes.InvalidArgument {
				return nil, status.Errorf(codes.InvalidArgument, "argument invalid %v", err)
			} else if errStatus.Code() == codes.NotFound {
				return nil, nil
			}
			// errStatus.Code() == codes.Internal = retry
		} else if ctx.Err() != nil {
			s.Emailsreco <- true
		} else {
			return grp, nil
		}
	}
	return nil, status.Errorf(codes.NotFound, "Email not send")
}
