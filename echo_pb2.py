# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo.proto',
  package='echo',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\necho.proto\x12\x04\x65\x63ho\"2\n\x0b\x45\x63hoRequest\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x15\n\rrepetitionNum\x18\x02 \x01(\x05\"\x1d\n\nEchoReplay\x12\x0f\n\x07message\x18\x01 \x01(\t2h\n\x04\x45\x63ho\x12-\n\x04\x45\x63ho\x12\x11.echo.EchoRequest\x1a\x10.echo.EchoReplay\"\x00\x12\x31\n\x08\x45\x63hoMany\x12\x11.echo.EchoRequest\x1a\x10.echo.EchoReplay\"\x00\x62\x06proto3'
)




_ECHOREQUEST = _descriptor.Descriptor(
  name='EchoRequest',
  full_name='echo.EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='echo.EchoRequest.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repetitionNum', full_name='echo.EchoRequest.repetitionNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=70,
)


_ECHOREPLAY = _descriptor.Descriptor(
  name='EchoReplay',
  full_name='echo.EchoReplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='echo.EchoReplay.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoReplay'] = _ECHOREPLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EchoRequest = _reflection.GeneratedProtocolMessageType('EchoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoRequest)
  })
_sym_db.RegisterMessage(EchoRequest)

EchoReplay = _reflection.GeneratedProtocolMessageType('EchoReplay', (_message.Message,), {
  'DESCRIPTOR' : _ECHOREPLAY,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:echo.EchoReplay)
  })
_sym_db.RegisterMessage(EchoReplay)



_ECHO = _descriptor.ServiceDescriptor(
  name='Echo',
  full_name='echo.Echo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=103,
  serialized_end=207,
  methods=[
  _descriptor.MethodDescriptor(
    name='Echo',
    full_name='echo.Echo.Echo',
    index=0,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHOREPLAY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EchoMany',
    full_name='echo.Echo.EchoMany',
    index=1,
    containing_service=None,
    input_type=_ECHOREQUEST,
    output_type=_ECHOREPLAY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHO)

DESCRIPTOR.services_by_name['Echo'] = _ECHO

# @@protoc_insertion_point(module_scope)
