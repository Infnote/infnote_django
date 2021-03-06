# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manage.proto',
  package='manage',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cmanage.proto\x12\x06manage\"\x1c\n\x0bPeerRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"H\n\x0cPeerResponse\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\x0c\n\x04last\x18\x03 \x01(\x03\x12\x0e\n\x06server\x18\x04 \x01(\x08\"\x1a\n\x0c\x43hainRequest\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\rChainResponse\x12\x0b\n\x03ref\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\"9\n\x0c\x42lockRequest\x12\x0f\n\x07\x63hainID\x18\x01 \x01(\t\x12\x0c\n\x04\x66rom\x18\x02 \x01(\x04\x12\n\n\x02to\x18\x03 \x01(\x04\"q\n\rBlockResponse\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0c\n\x04time\x18\x02 \x01(\x04\x12\x10\n\x08prevHash\x18\x03 \x01(\t\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t\x12\x0f\n\x07payload\x18\x06 \x01(\x0c\"b\n\x14\x43hainCreationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x05 \x01(\t\"=\n\x15\x43hainCreationResponse\x12\x0b\n\x03ref\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03wif\x18\x03 \x01(\t\"8\n\x14\x42lockCreationRequest\x12\x0f\n\x07\x63hainID\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"h\n\x15\x42lockCreationResponse\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x0c\n\x04time\x18\x02 \x01(\x04\x12\x10\n\x08prevHash\x18\x03 \x01(\t\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x05 \x01(\t2\xd4\x02\n\tIFCManage\x12\x37\n\x08GetPeers\x12\x13.manage.PeerRequest\x1a\x14.manage.PeerResponse0\x01\x12:\n\tGetChains\x12\x14.manage.ChainRequest\x1a\x15.manage.ChainResponse0\x01\x12:\n\tGetBlocks\x12\x14.manage.BlockRequest\x1a\x15.manage.BlockResponse0\x01\x12J\n\x0b\x43reateChain\x12\x1c.manage.ChainCreationRequest\x1a\x1d.manage.ChainCreationResponse\x12J\n\x0b\x43reateBlock\x12\x1c.manage.BlockCreationRequest\x1a\x1d.manage.BlockCreationResponseb\x06proto3')
)




_PEERREQUEST = _descriptor.Descriptor(
  name='PeerRequest',
  full_name='manage.PeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='manage.PeerRequest.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=24,
  serialized_end=52,
)


_PEERRESPONSE = _descriptor.Descriptor(
  name='PeerResponse',
  full_name='manage.PeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='manage.PeerResponse.addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='manage.PeerResponse.rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last', full_name='manage.PeerResponse.last', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server', full_name='manage.PeerResponse.server', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=54,
  serialized_end=126,
)


_CHAINREQUEST = _descriptor.Descriptor(
  name='ChainRequest',
  full_name='manage.ChainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='manage.ChainRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=128,
  serialized_end=154,
)


_CHAINRESPONSE = _descriptor.Descriptor(
  name='ChainResponse',
  full_name='manage.ChainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ref', full_name='manage.ChainResponse.ref', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='manage.ChainResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='manage.ChainResponse.count', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=156,
  serialized_end=211,
)


_BLOCKREQUEST = _descriptor.Descriptor(
  name='BlockRequest',
  full_name='manage.BlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chainID', full_name='manage.BlockRequest.chainID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from', full_name='manage.BlockRequest.from', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='manage.BlockRequest.to', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=213,
  serialized_end=270,
)


_BLOCKRESPONSE = _descriptor.Descriptor(
  name='BlockResponse',
  full_name='manage.BlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='manage.BlockResponse.height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='manage.BlockResponse.time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevHash', full_name='manage.BlockResponse.prevHash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='manage.BlockResponse.hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='manage.BlockResponse.signature', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='manage.BlockResponse.payload', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=272,
  serialized_end=385,
)


_CHAINCREATIONREQUEST = _descriptor.Descriptor(
  name='ChainCreationRequest',
  full_name='manage.ChainCreationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='manage.ChainCreationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='manage.ChainCreationRequest.author', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='website', full_name='manage.ChainCreationRequest.website', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='manage.ChainCreationRequest.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='manage.ChainCreationRequest.desc', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=387,
  serialized_end=485,
)


_CHAINCREATIONRESPONSE = _descriptor.Descriptor(
  name='ChainCreationResponse',
  full_name='manage.ChainCreationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ref', full_name='manage.ChainCreationResponse.ref', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='manage.ChainCreationResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wif', full_name='manage.ChainCreationResponse.wif', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=487,
  serialized_end=548,
)


_BLOCKCREATIONREQUEST = _descriptor.Descriptor(
  name='BlockCreationRequest',
  full_name='manage.BlockCreationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chainID', full_name='manage.BlockCreationRequest.chainID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='manage.BlockCreationRequest.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=550,
  serialized_end=606,
)


_BLOCKCREATIONRESPONSE = _descriptor.Descriptor(
  name='BlockCreationResponse',
  full_name='manage.BlockCreationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='manage.BlockCreationResponse.height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='manage.BlockCreationResponse.time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevHash', full_name='manage.BlockCreationResponse.prevHash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='manage.BlockCreationResponse.hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='manage.BlockCreationResponse.signature', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=608,
  serialized_end=712,
)

DESCRIPTOR.message_types_by_name['PeerRequest'] = _PEERREQUEST
DESCRIPTOR.message_types_by_name['PeerResponse'] = _PEERRESPONSE
DESCRIPTOR.message_types_by_name['ChainRequest'] = _CHAINREQUEST
DESCRIPTOR.message_types_by_name['ChainResponse'] = _CHAINRESPONSE
DESCRIPTOR.message_types_by_name['BlockRequest'] = _BLOCKREQUEST
DESCRIPTOR.message_types_by_name['BlockResponse'] = _BLOCKRESPONSE
DESCRIPTOR.message_types_by_name['ChainCreationRequest'] = _CHAINCREATIONREQUEST
DESCRIPTOR.message_types_by_name['ChainCreationResponse'] = _CHAINCREATIONRESPONSE
DESCRIPTOR.message_types_by_name['BlockCreationRequest'] = _BLOCKCREATIONREQUEST
DESCRIPTOR.message_types_by_name['BlockCreationResponse'] = _BLOCKCREATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PeerRequest = _reflection.GeneratedProtocolMessageType('PeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _PEERREQUEST,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.PeerRequest)
  ))
_sym_db.RegisterMessage(PeerRequest)

PeerResponse = _reflection.GeneratedProtocolMessageType('PeerResponse', (_message.Message,), dict(
  DESCRIPTOR = _PEERRESPONSE,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.PeerResponse)
  ))
_sym_db.RegisterMessage(PeerResponse)

ChainRequest = _reflection.GeneratedProtocolMessageType('ChainRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHAINREQUEST,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.ChainRequest)
  ))
_sym_db.RegisterMessage(ChainRequest)

ChainResponse = _reflection.GeneratedProtocolMessageType('ChainResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHAINRESPONSE,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.ChainResponse)
  ))
_sym_db.RegisterMessage(ChainResponse)

BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKREQUEST,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.BlockRequest)
  ))
_sym_db.RegisterMessage(BlockRequest)

BlockResponse = _reflection.GeneratedProtocolMessageType('BlockResponse', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKRESPONSE,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.BlockResponse)
  ))
_sym_db.RegisterMessage(BlockResponse)

ChainCreationRequest = _reflection.GeneratedProtocolMessageType('ChainCreationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCREATIONREQUEST,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.ChainCreationRequest)
  ))
_sym_db.RegisterMessage(ChainCreationRequest)

ChainCreationResponse = _reflection.GeneratedProtocolMessageType('ChainCreationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCREATIONRESPONSE,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.ChainCreationResponse)
  ))
_sym_db.RegisterMessage(ChainCreationResponse)

BlockCreationRequest = _reflection.GeneratedProtocolMessageType('BlockCreationRequest', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKCREATIONREQUEST,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.BlockCreationRequest)
  ))
_sym_db.RegisterMessage(BlockCreationRequest)

BlockCreationResponse = _reflection.GeneratedProtocolMessageType('BlockCreationResponse', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKCREATIONRESPONSE,
  __module__ = 'manage_pb2'
  # @@protoc_insertion_point(class_scope:manage.BlockCreationResponse)
  ))
_sym_db.RegisterMessage(BlockCreationResponse)



_IFCMANAGE = _descriptor.ServiceDescriptor(
  name='IFCManage',
  full_name='manage.IFCManage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=715,
  serialized_end=1055,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPeers',
    full_name='manage.IFCManage.GetPeers',
    index=0,
    containing_service=None,
    input_type=_PEERREQUEST,
    output_type=_PEERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetChains',
    full_name='manage.IFCManage.GetChains',
    index=1,
    containing_service=None,
    input_type=_CHAINREQUEST,
    output_type=_CHAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBlocks',
    full_name='manage.IFCManage.GetBlocks',
    index=2,
    containing_service=None,
    input_type=_BLOCKREQUEST,
    output_type=_BLOCKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateChain',
    full_name='manage.IFCManage.CreateChain',
    index=3,
    containing_service=None,
    input_type=_CHAINCREATIONREQUEST,
    output_type=_CHAINCREATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateBlock',
    full_name='manage.IFCManage.CreateBlock',
    index=4,
    containing_service=None,
    input_type=_BLOCKCREATIONREQUEST,
    output_type=_BLOCKCREATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IFCMANAGE)

DESCRIPTOR.services_by_name['IFCManage'] = _IFCMANAGE

# @@protoc_insertion_point(module_scope)
