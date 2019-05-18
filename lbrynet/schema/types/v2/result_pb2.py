# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='result.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cresult.proto\x12\x02pb\"B\n\x07Outputs\x12\x18\n\x04txos\x18\x01 \x03(\x0b\x32\n.pb.Output\x12\r\n\x05total\x18\x02 \x01(\r\x12\x0e\n\x06offset\x18\x03 \x01(\r\"{\n\x06Output\x12\x0f\n\x07tx_hash\x18\x01 \x01(\x0c\x12\x0c\n\x04nout\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x1e\n\x05\x63laim\x18\x07 \x01(\x0b\x32\r.pb.ClaimMetaH\x00\x12\x1a\n\x05\x65rror\x18\x0f \x01(\x0b\x32\t.pb.ErrorH\x00\x42\x06\n\x04meta\"\x89\x02\n\tClaimMeta\x12\x1b\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\n.pb.Output\x12\x16\n\x0eis_controlling\x18\x02 \x01(\x08\x12\x19\n\x11\x61\x63tivation_height\x18\x03 \x01(\r\x12\x18\n\x10\x65\x66\x66\x65\x63tive_amount\x18\x04 \x01(\x04\x12\x16\n\x0esupport_amount\x18\x05 \x01(\x04\x12\x19\n\x11\x63laims_in_channel\x18\x06 \x01(\r\x12\x16\n\x0etrending_group\x18\x07 \x01(\r\x12\x16\n\x0etrending_mixed\x18\x08 \x01(\x12\x12\x16\n\x0etrending_local\x18\t \x01(\x12\x12\x17\n\x0ftrending_global\x18\n \x01(\x12\"i\n\x05\x45rror\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.pb.Error.Code\x12\x0c\n\x04text\x18\x02 \x01(\t\"4\n\x04\x43ode\x12\x10\n\x0cUNKNOWN_CODE\x10\x00\x12\r\n\tNOT_FOUND\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x62\x06proto3')
)



_ERROR_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='pb.Error.Code',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CODE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=534,
  serialized_end=586,
)
_sym_db.RegisterEnumDescriptor(_ERROR_CODE)


_OUTPUTS = _descriptor.Descriptor(
  name='Outputs',
  full_name='pb.Outputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txos', full_name='pb.Outputs.txos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='pb.Outputs.total', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='pb.Outputs.offset', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=86,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='pb.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='pb.Output.tx_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nout', full_name='pb.Output.nout', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='pb.Output.height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claim', full_name='pb.Output.claim', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pb.Output.error', index=4,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='meta', full_name='pb.Output.meta',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=88,
  serialized_end=211,
)


_CLAIMMETA = _descriptor.Descriptor(
  name='ClaimMeta',
  full_name='pb.ClaimMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='pb.ClaimMeta.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_controlling', full_name='pb.ClaimMeta.is_controlling', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activation_height', full_name='pb.ClaimMeta.activation_height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effective_amount', full_name='pb.ClaimMeta.effective_amount', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='support_amount', full_name='pb.ClaimMeta.support_amount', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claims_in_channel', full_name='pb.ClaimMeta.claims_in_channel', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trending_group', full_name='pb.ClaimMeta.trending_group', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trending_mixed', full_name='pb.ClaimMeta.trending_mixed', index=7,
      number=8, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trending_local', full_name='pb.ClaimMeta.trending_local', index=8,
      number=9, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trending_global', full_name='pb.ClaimMeta.trending_global', index=9,
      number=10, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=214,
  serialized_end=479,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='pb.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pb.Error.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='pb.Error.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERROR_CODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=586,
)

_OUTPUTS.fields_by_name['txos'].message_type = _OUTPUT
_OUTPUT.fields_by_name['claim'].message_type = _CLAIMMETA
_OUTPUT.fields_by_name['error'].message_type = _ERROR
_OUTPUT.oneofs_by_name['meta'].fields.append(
  _OUTPUT.fields_by_name['claim'])
_OUTPUT.fields_by_name['claim'].containing_oneof = _OUTPUT.oneofs_by_name['meta']
_OUTPUT.oneofs_by_name['meta'].fields.append(
  _OUTPUT.fields_by_name['error'])
_OUTPUT.fields_by_name['error'].containing_oneof = _OUTPUT.oneofs_by_name['meta']
_CLAIMMETA.fields_by_name['channel'].message_type = _OUTPUT
_ERROR.fields_by_name['code'].enum_type = _ERROR_CODE
_ERROR_CODE.containing_type = _ERROR
DESCRIPTOR.message_types_by_name['Outputs'] = _OUTPUTS
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['ClaimMeta'] = _CLAIMMETA
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Outputs = _reflection.GeneratedProtocolMessageType('Outputs', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTS,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.Outputs)
  ))
_sym_db.RegisterMessage(Outputs)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUT,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.Output)
  ))
_sym_db.RegisterMessage(Output)

ClaimMeta = _reflection.GeneratedProtocolMessageType('ClaimMeta', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMMETA,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.ClaimMeta)
  ))
_sym_db.RegisterMessage(ClaimMeta)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'result_pb2'
  # @@protoc_insertion_point(class_scope:pb.Error)
  ))
_sym_db.RegisterMessage(Error)


# @@protoc_insertion_point(module_scope)
