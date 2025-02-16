# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qscmining.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qsc.generated.qsc_pb2 as qsc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fqscmining.proto\x12\x03qsc\x1a\tqsc.proto\"-\n\x1bGetBlockMiningCompatibleReq\x12\x0e\n\x06height\x18\x01 \x01(\x04\"\'\n\x15GetLastBlockHeaderReq\x12\x0e\n\x06height\x18\x01 \x01(\x04\"p\n\x1cGetBlockMiningCompatibleResp\x12%\n\x0b\x62lockheader\x18\x01 \x01(\x0b\x32\x10.qsc.BlockHeader\x12)\n\rblockmetadata\x18\x02 \x01(\x0b\x32\x12.qsc.BlockMetaData\"|\n\x16GetLastBlockHeaderResp\x12\x12\n\ndifficulty\x18\x01 \x01(\x04\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x12\x0e\n\x06reward\x18\x04 \x01(\x04\x12\x0c\n\x04hash\x18\x05 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x06 \x01(\x04\"+\n\x11GetBlockToMineReq\x12\x16\n\x0ewallet_address\x18\x01 \x01(\x0c\"\x80\x01\n\x12GetBlockToMineResp\x12\x1a\n\x12\x62locktemplate_blob\x18\x01 \x01(\t\x12\x12\n\ndifficulty\x18\x02 \x01(\x04\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\x17\n\x0freserved_offset\x18\x04 \x01(\r\x12\x11\n\tseed_hash\x18\x05 \x01(\t\"#\n\x13SubmitMinedBlockReq\x12\x0c\n\x04\x62lob\x18\x01 \x01(\x0c\"%\n\x14SubmitMinedBlockResp\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x32\xc7\x02\n\tMiningAPI\x12_\n\x18GetBlockMiningCompatible\x12 .qsc.GetBlockMiningCompatibleReq\x1a!.qsc.GetBlockMiningCompatibleResp\x12M\n\x12GetLastBlockHeader\x12\x1a.qsc.GetLastBlockHeaderReq\x1a\x1b.qsc.GetLastBlockHeaderResp\x12\x41\n\x0eGetBlockToMine\x12\x16.qsc.GetBlockToMineReq\x1a\x17.qsc.GetBlockToMineResp\x12G\n\x10SubmitMinedBlock\x12\x18.qsc.SubmitMinedBlockReq\x1a\x19.qsc.SubmitMinedBlockRespb\x06proto3')



_GETBLOCKMININGCOMPATIBLEREQ = DESCRIPTOR.message_types_by_name['GetBlockMiningCompatibleReq']
_GETLASTBLOCKHEADERREQ = DESCRIPTOR.message_types_by_name['GetLastBlockHeaderReq']
_GETBLOCKMININGCOMPATIBLERESP = DESCRIPTOR.message_types_by_name['GetBlockMiningCompatibleResp']
_GETLASTBLOCKHEADERRESP = DESCRIPTOR.message_types_by_name['GetLastBlockHeaderResp']
_GETBLOCKTOMINEREQ = DESCRIPTOR.message_types_by_name['GetBlockToMineReq']
_GETBLOCKTOMINERESP = DESCRIPTOR.message_types_by_name['GetBlockToMineResp']
_SUBMITMINEDBLOCKREQ = DESCRIPTOR.message_types_by_name['SubmitMinedBlockReq']
_SUBMITMINEDBLOCKRESP = DESCRIPTOR.message_types_by_name['SubmitMinedBlockResp']
GetBlockMiningCompatibleReq = _reflection.GeneratedProtocolMessageType('GetBlockMiningCompatibleReq', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKMININGCOMPATIBLEREQ,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.GetBlockMiningCompatibleReq)
  })
_sym_db.RegisterMessage(GetBlockMiningCompatibleReq)

GetLastBlockHeaderReq = _reflection.GeneratedProtocolMessageType('GetLastBlockHeaderReq', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTBLOCKHEADERREQ,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.GetLastBlockHeaderReq)
  })
_sym_db.RegisterMessage(GetLastBlockHeaderReq)

GetBlockMiningCompatibleResp = _reflection.GeneratedProtocolMessageType('GetBlockMiningCompatibleResp', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKMININGCOMPATIBLERESP,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.GetBlockMiningCompatibleResp)
  })
_sym_db.RegisterMessage(GetBlockMiningCompatibleResp)

GetLastBlockHeaderResp = _reflection.GeneratedProtocolMessageType('GetLastBlockHeaderResp', (_message.Message,), {
  'DESCRIPTOR' : _GETLASTBLOCKHEADERRESP,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.GetLastBlockHeaderResp)
  })
_sym_db.RegisterMessage(GetLastBlockHeaderResp)

GetBlockToMineReq = _reflection.GeneratedProtocolMessageType('GetBlockToMineReq', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKTOMINEREQ,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.GetBlockToMineReq)
  })
_sym_db.RegisterMessage(GetBlockToMineReq)

GetBlockToMineResp = _reflection.GeneratedProtocolMessageType('GetBlockToMineResp', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKTOMINERESP,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.GetBlockToMineResp)
  })
_sym_db.RegisterMessage(GetBlockToMineResp)

SubmitMinedBlockReq = _reflection.GeneratedProtocolMessageType('SubmitMinedBlockReq', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITMINEDBLOCKREQ,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.SubmitMinedBlockReq)
  })
_sym_db.RegisterMessage(SubmitMinedBlockReq)

SubmitMinedBlockResp = _reflection.GeneratedProtocolMessageType('SubmitMinedBlockResp', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITMINEDBLOCKRESP,
  '__module__' : 'qscmining_pb2'
  # @@protoc_insertion_point(class_scope:qsc.SubmitMinedBlockResp)
  })
_sym_db.RegisterMessage(SubmitMinedBlockResp)

_MININGAPI = DESCRIPTOR.services_by_name['MiningAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETBLOCKMININGCOMPATIBLEREQ._serialized_start=35
  _GETBLOCKMININGCOMPATIBLEREQ._serialized_end=80
  _GETLASTBLOCKHEADERREQ._serialized_start=82
  _GETLASTBLOCKHEADERREQ._serialized_end=121
  _GETBLOCKMININGCOMPATIBLERESP._serialized_start=123
  _GETBLOCKMININGCOMPATIBLERESP._serialized_end=235
  _GETLASTBLOCKHEADERRESP._serialized_start=237
  _GETLASTBLOCKHEADERRESP._serialized_end=361
  _GETBLOCKTOMINEREQ._serialized_start=363
  _GETBLOCKTOMINEREQ._serialized_end=406
  _GETBLOCKTOMINERESP._serialized_start=409
  _GETBLOCKTOMINERESP._serialized_end=537
  _SUBMITMINEDBLOCKREQ._serialized_start=539
  _SUBMITMINEDBLOCKREQ._serialized_end=574
  _SUBMITMINEDBLOCKRESP._serialized_start=576
  _SUBMITMINEDBLOCKRESP._serialized_end=613
  _MININGAPI._serialized_start=616
  _MININGAPI._serialized_end=943
# @@protoc_insertion_point(module_scope)
