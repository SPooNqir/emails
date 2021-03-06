# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: emails.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='emails.proto',
  package='emails',
  syntax='proto3',
  serialized_options=b'Z\032github.com/SPooNqir/emails\222A\226\004\022\210\001\n\030Spoon - Emails Golang WS\"e\n\020Spoon Cloud Team\0221https://gitlab.com/SpoonQIR/Cloud/services/emails\032\036sebastien.lavayssiere@spoon.ai2\0050.0.1*\002\002\0012\020application/json:\020application/jsonRP\n\003403\022I\nGReturned when the user does not have permission to access the resource.R;\n\003404\0224\n*Returned when the resource does not exist.\022\006\n\004\232\002\001\007RW\n\003418\022P\n\rI\'m a teapot.\022?\n=\032;.grpc.gateway.examples.internal.proto.examplepb.NumericEnumZ#\n!\n\nApiKeyAuth\022\023\010\002\032\rAuthorization \002b\020\n\016\n\nApiKeyAuth\022\000rB\n\rlink for docs\0221https://gitlab.com/SpoonQIR/Cloud/services/emails',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x65mails.proto\x12\x06\x65mails\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x19google/protobuf/any.proto\"\x9f\x01\n\rEmailTemplate\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03tos\x18\x02 \x03(\t\x12\x35\n\x08replaces\x18\x03 \x03(\x0b\x32#.emails.EmailTemplate.ReplacesEntry\x12\x0c\n\x04\x66rom\x18\x04 \x01(\t\x1a/\n\rReplacesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32]\n\x06\x45mails\x12S\n\x0cSendTemplate\x12\x15.emails.EmailTemplate\x1a\x15.emails.EmailTemplate\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/v1/emails:\x01*B\xb6\x04Z\x1agithub.com/SPooNqir/emails\x92\x41\x96\x04\x12\x88\x01\n\x18Spoon - Emails Golang WS\"e\n\x10Spoon Cloud Team\x12\x31https://gitlab.com/SpoonQIR/Cloud/services/emails\x1a\x1esebastien.lavayssiere@spoon.ai2\x05\x30.0.1*\x02\x02\x01\x32\x10\x61pplication/json:\x10\x61pplication/jsonRP\n\x03\x34\x30\x33\x12I\nGReturned when the user does not have permission to access the resource.R;\n\x03\x34\x30\x34\x12\x34\n*Returned when the resource does not exist.\x12\x06\n\x04\x9a\x02\x01\x07RW\n\x03\x34\x31\x38\x12P\n\rI\'m a teapot.\x12?\n=\x1a;.grpc.gateway.examples.internal.proto.examplepb.NumericEnumZ#\n!\n\nApiKeyAuth\x12\x13\x08\x02\x1a\rAuthorization \x02\x62\x10\n\x0e\n\nApiKeyAuth\x12\x00rB\n\rlink for docs\x12\x31https://gitlab.com/SpoonQIR/Cloud/services/emailsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_EMAILTEMPLATE_REPLACESENTRY = _descriptor.Descriptor(
  name='ReplacesEntry',
  full_name='emails.EmailTemplate.ReplacesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='emails.EmailTemplate.ReplacesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='emails.EmailTemplate.ReplacesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=289,
)

_EMAILTEMPLATE = _descriptor.Descriptor(
  name='EmailTemplate',
  full_name='emails.EmailTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='emails.EmailTemplate.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tos', full_name='emails.EmailTemplate.tos', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='replaces', full_name='emails.EmailTemplate.replaces', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from', full_name='emails.EmailTemplate.from', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EMAILTEMPLATE_REPLACESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=289,
)

_EMAILTEMPLATE_REPLACESENTRY.containing_type = _EMAILTEMPLATE
_EMAILTEMPLATE.fields_by_name['replaces'].message_type = _EMAILTEMPLATE_REPLACESENTRY
DESCRIPTOR.message_types_by_name['EmailTemplate'] = _EMAILTEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmailTemplate = _reflection.GeneratedProtocolMessageType('EmailTemplate', (_message.Message,), {

  'ReplacesEntry' : _reflection.GeneratedProtocolMessageType('ReplacesEntry', (_message.Message,), {
    'DESCRIPTOR' : _EMAILTEMPLATE_REPLACESENTRY,
    '__module__' : 'emails_pb2'
    # @@protoc_insertion_point(class_scope:emails.EmailTemplate.ReplacesEntry)
    })
  ,
  'DESCRIPTOR' : _EMAILTEMPLATE,
  '__module__' : 'emails_pb2'
  # @@protoc_insertion_point(class_scope:emails.EmailTemplate)
  })
_sym_db.RegisterMessage(EmailTemplate)
_sym_db.RegisterMessage(EmailTemplate.ReplacesEntry)


DESCRIPTOR._options = None
_EMAILTEMPLATE_REPLACESENTRY._options = None

_EMAILS = _descriptor.ServiceDescriptor(
  name='Emails',
  full_name='emails.Emails',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=291,
  serialized_end=384,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendTemplate',
    full_name='emails.Emails.SendTemplate',
    index=0,
    containing_service=None,
    input_type=_EMAILTEMPLATE,
    output_type=_EMAILTEMPLATE,
    serialized_options=b'\202\323\344\223\002\017\"\n/v1/emails:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EMAILS)

DESCRIPTOR.services_by_name['Emails'] = _EMAILS

# @@protoc_insertion_point(module_scope)
