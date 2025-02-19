# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qscstateinfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qsc.generated.qsc_pb2 as qsc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12qscstateinfo.proto\x12\x03qsc\x1a\tqsc.proto\"e\n\x13TransactionMetadata\x12%\n\x0btransaction\x18\x01 \x01(\x0b\x32\x10.qsc.Transaction\x12\x14\n\x0c\x62lock_number\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"A\n\x10LastTransactions\x12-\n\x0btx_metadata\x18\x01 \x03(\x0b\x32\x18.qsc.TransactionMetadata\"\x8a\x01\n\tForkState\x12\x1c\n\x14initiator_headerhash\x18\x01 \x01(\x0c\x12\x1d\n\x15\x66ork_point_headerhash\x18\x02 \x01(\x0c\x12\x1f\n\x17old_mainchain_hash_path\x18\x03 \x03(\x0c\x12\x1f\n\x17new_mainchain_hash_path\x18\x04 \x03(\x0c\x62\x06proto3')



_TRANSACTIONMETADATA = DESCRIPTOR.message_types_by_name['TransactionMetadata']
_LASTTRANSACTIONS = DESCRIPTOR.message_types_by_name['LastTransactions']
_FORKSTATE = DESCRIPTOR.message_types_by_name['ForkState']
TransactionMetadata = _reflection.GeneratedProtocolMessageType('TransactionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONMETADATA,
  '__module__' : 'qscstateinfo_pb2'
  # @@protoc_insertion_point(class_scope:qsc.TransactionMetadata)
  })
_sym_db.RegisterMessage(TransactionMetadata)

LastTransactions = _reflection.GeneratedProtocolMessageType('LastTransactions', (_message.Message,), {
  'DESCRIPTOR' : _LASTTRANSACTIONS,
  '__module__' : 'qscstateinfo_pb2'
  # @@protoc_insertion_point(class_scope:qsc.LastTransactions)
  })
_sym_db.RegisterMessage(LastTransactions)

ForkState = _reflection.GeneratedProtocolMessageType('ForkState', (_message.Message,), {
  'DESCRIPTOR' : _FORKSTATE,
  '__module__' : 'qscstateinfo_pb2'
  # @@protoc_insertion_point(class_scope:qsc.ForkState)
  })
_sym_db.RegisterMessage(ForkState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRANSACTIONMETADATA._serialized_start=38
  _TRANSACTIONMETADATA._serialized_end=139
  _LASTTRANSACTIONS._serialized_start=141
  _LASTTRANSACTIONS._serialized_end=206
  _FORKSTATE._serialized_start=209
  _FORKSTATE._serialized_end=347
# @@protoc_insertion_point(module_scope)
