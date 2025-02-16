# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qsclegacy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qsc.generated.qsc_pb2 as qsc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fqsclegacy.proto\x12\x03qsc\x1a\tqsc.proto\"\xf2\x08\n\rLegacyMessage\x12.\n\tfunc_name\x18\x01 \x01(\x0e\x32\x1b.qsc.LegacyMessage.FuncName\x12\x1d\n\x06noData\x18\x02 \x01(\x0b\x32\x0b.qsc.NoDataH\x00\x12\x1d\n\x06veData\x18\x03 \x01(\x0b\x32\x0b.qsc.VEDataH\x00\x12\x1d\n\x06plData\x18\x04 \x01(\x0b\x32\x0b.qsc.PLDataH\x00\x12!\n\x08pongData\x18\x05 \x01(\x0b\x32\r.qsc.PONGDataH\x00\x12\x1d\n\x06mrData\x18\x06 \x01(\x0b\x32\x0b.qsc.MRDataH\x00\x12\x1b\n\x05\x62lock\x18\x07 \x01(\x0b\x32\n.qsc.BlockH\x00\x12\x1d\n\x06\x66\x62\x44\x61ta\x18\x08 \x01(\x0b\x32\x0b.qsc.FBDataH\x00\x12\x1d\n\x06pbData\x18\t \x01(\x0b\x32\x0b.qsc.PBDataH\x00\x12&\n\x06\x62hData\x18\n \x01(\x0b\x32\x14.qsc.BlockHeightDataH\x00\x12\"\n\x06txData\x18\x0b \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\"\n\x06mtData\x18\x0c \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\"\n\x06tkData\x18\r \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\"\n\x06ttData\x18\x0e \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\"\n\x06ltData\x18\x0f \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\"\n\x06slData\x18\x10 \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\x31\n\x07\x65phData\x18\x11 \x01(\x0b\x32\x1e.qsc.EncryptedEphemeralMessageH\x00\x12!\n\x08syncData\x18\x12 \x01(\x0b\x32\r.qsc.SYNCDataH\x00\x12-\n\x0e\x63hainStateData\x18\x13 \x01(\x0b\x32\x13.qsc.NodeChainStateH\x00\x12-\n\x0enodeHeaderHash\x18\x14 \x01(\x0b\x32\x13.qsc.NodeHeaderHashH\x00\x12-\n\np2pAckData\x18\x15 \x01(\x0b\x32\x17.qsc.P2PAcknowledgementH\x00\x12\"\n\x06mcData\x18\x16 \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\"\n\x06msData\x18\x17 \x01(\x0b\x32\x10.qsc.TransactionH\x00\x12\"\n\x06mvData\x18\x18 \x01(\x0b\x32\x10.qsc.TransactionH\x00\"\xdf\x01\n\x08\x46uncName\x12\x06\n\x02VE\x10\x00\x12\x06\n\x02PL\x10\x01\x12\x08\n\x04PONG\x10\x02\x12\x06\n\x02MR\x10\x03\x12\x07\n\x03SFM\x10\x04\x12\x06\n\x02\x42K\x10\x05\x12\x06\n\x02\x46\x42\x10\x06\x12\x06\n\x02PB\x10\x07\x12\x06\n\x02\x42H\x10\x08\x12\x06\n\x02TX\x10\t\x12\x06\n\x02LT\x10\n\x12\x07\n\x03\x45PH\x10\x0b\x12\x06\n\x02MT\x10\x0c\x12\x06\n\x02TK\x10\r\x12\x06\n\x02TT\x10\x0e\x12\x06\n\x02SL\x10\x0f\x12\x08\n\x04SYNC\x10\x10\x12\x0e\n\nCHAINSTATE\x10\x11\x12\x10\n\x0cHEADERHASHES\x10\x12\x12\x0b\n\x07P2P_ACK\x10\x13\x12\x06\n\x02MC\x10\x14\x12\x06\n\x02MS\x10\x15\x12\x06\n\x02MV\x10\x16\x42\x06\n\x04\x64\x61ta\"\x08\n\x06NoData\"H\n\x06VEData\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x19\n\x11genesis_prev_hash\x18\x02 \x01(\x0c\x12\x12\n\nrate_limit\x18\x03 \x01(\x04\"/\n\x06PLData\x12\x10\n\x08peer_ips\x18\x01 \x03(\t\x12\x13\n\x0bpublic_port\x18\x02 \x01(\r\"\n\n\x08PONGData\"\x9d\x01\n\x06MRData\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.qsc.LegacyMessage.FuncName\x12\x16\n\x0estake_selector\x18\x03 \x01(\x0c\x12\x14\n\x0c\x62lock_number\x18\x04 \x01(\x04\x12\x17\n\x0fprev_headerhash\x18\x05 \x01(\x0c\x12\x13\n\x0breveal_hash\x18\x06 \x01(\x0c\"@\n\x06\x42KData\x12\x1b\n\x06mrData\x18\x01 \x01(\x0b\x32\x0b.qsc.MRData\x12\x19\n\x05\x62lock\x18\x02 \x01(\x0b\x32\n.qsc.Block\"\x17\n\x06\x46\x42\x44\x61ta\x12\r\n\x05index\x18\x01 \x01(\x04\"#\n\x06PBData\x12\x19\n\x05\x62lock\x18\x01 \x01(\x0b\x32\n.qsc.Block\"\x19\n\x08SYNCData\x12\r\n\x05state\x18\x01 \x01(\tb\x06proto3')



_LEGACYMESSAGE = DESCRIPTOR.message_types_by_name['LegacyMessage']
_NODATA = DESCRIPTOR.message_types_by_name['NoData']
_VEDATA = DESCRIPTOR.message_types_by_name['VEData']
_PLDATA = DESCRIPTOR.message_types_by_name['PLData']
_PONGDATA = DESCRIPTOR.message_types_by_name['PONGData']
_MRDATA = DESCRIPTOR.message_types_by_name['MRData']
_BKDATA = DESCRIPTOR.message_types_by_name['BKData']
_FBDATA = DESCRIPTOR.message_types_by_name['FBData']
_PBDATA = DESCRIPTOR.message_types_by_name['PBData']
_SYNCDATA = DESCRIPTOR.message_types_by_name['SYNCData']
_LEGACYMESSAGE_FUNCNAME = _LEGACYMESSAGE.enum_types_by_name['FuncName']
LegacyMessage = _reflection.GeneratedProtocolMessageType('LegacyMessage', (_message.Message,), {
  'DESCRIPTOR' : _LEGACYMESSAGE,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.LegacyMessage)
  })
_sym_db.RegisterMessage(LegacyMessage)

NoData = _reflection.GeneratedProtocolMessageType('NoData', (_message.Message,), {
  'DESCRIPTOR' : _NODATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.NoData)
  })
_sym_db.RegisterMessage(NoData)

VEData = _reflection.GeneratedProtocolMessageType('VEData', (_message.Message,), {
  'DESCRIPTOR' : _VEDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.VEData)
  })
_sym_db.RegisterMessage(VEData)

PLData = _reflection.GeneratedProtocolMessageType('PLData', (_message.Message,), {
  'DESCRIPTOR' : _PLDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.PLData)
  })
_sym_db.RegisterMessage(PLData)

PONGData = _reflection.GeneratedProtocolMessageType('PONGData', (_message.Message,), {
  'DESCRIPTOR' : _PONGDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.PONGData)
  })
_sym_db.RegisterMessage(PONGData)

MRData = _reflection.GeneratedProtocolMessageType('MRData', (_message.Message,), {
  'DESCRIPTOR' : _MRDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.MRData)
  })
_sym_db.RegisterMessage(MRData)

BKData = _reflection.GeneratedProtocolMessageType('BKData', (_message.Message,), {
  'DESCRIPTOR' : _BKDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.BKData)
  })
_sym_db.RegisterMessage(BKData)

FBData = _reflection.GeneratedProtocolMessageType('FBData', (_message.Message,), {
  'DESCRIPTOR' : _FBDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.FBData)
  })
_sym_db.RegisterMessage(FBData)

PBData = _reflection.GeneratedProtocolMessageType('PBData', (_message.Message,), {
  'DESCRIPTOR' : _PBDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.PBData)
  })
_sym_db.RegisterMessage(PBData)

SYNCData = _reflection.GeneratedProtocolMessageType('SYNCData', (_message.Message,), {
  'DESCRIPTOR' : _SYNCDATA,
  '__module__' : 'qsclegacy_pb2'
  # @@protoc_insertion_point(class_scope:qsc.SYNCData)
  })
_sym_db.RegisterMessage(SYNCData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LEGACYMESSAGE._serialized_start=36
  _LEGACYMESSAGE._serialized_end=1174
  _LEGACYMESSAGE_FUNCNAME._serialized_start=943
  _LEGACYMESSAGE_FUNCNAME._serialized_end=1166
  _NODATA._serialized_start=1176
  _NODATA._serialized_end=1184
  _VEDATA._serialized_start=1186
  _VEDATA._serialized_end=1258
  _PLDATA._serialized_start=1260
  _PLDATA._serialized_end=1307
  _PONGDATA._serialized_start=1309
  _PONGDATA._serialized_end=1319
  _MRDATA._serialized_start=1322
  _MRDATA._serialized_end=1479
  _BKDATA._serialized_start=1481
  _BKDATA._serialized_end=1545
  _FBDATA._serialized_start=1547
  _FBDATA._serialized_end=1570
  _PBDATA._serialized_start=1572
  _PBDATA._serialized_end=1607
  _SYNCDATA._serialized_start=1609
  _SYNCDATA._serialized_end=1634
# @@protoc_insertion_point(module_scope)
