# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_stream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64\x61ta_stream.proto\x12\x0b\x64\x61ta_stream\x1a\x1fgoogle/protobuf/timestamp.proto\"\x19\n\x04\x44\x61ta\x12\x11\n\tclient_id\x18\x01 \x01(\x03\"g\n\x0c\x44\x61taResponse\x12\x11\n\tserver_id\x18\x01 \x01(\x03\x12\x15\n\rresponse_data\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2V\n\nDataStream\x12H\n\x14\x44\x61taStreamingService\x12\x11.data_stream.Data\x1a\x19.data_stream.DataResponse\"\x00\x30\x01\x62\x06proto3')



_DATA = DESCRIPTOR.message_types_by_name['Data']
_DATARESPONSE = DESCRIPTOR.message_types_by_name['DataResponse']
Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'data_stream_pb2'
  # @@protoc_insertion_point(class_scope:data_stream.Data)
  })
_sym_db.RegisterMessage(Data)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATARESPONSE,
  '__module__' : 'data_stream_pb2'
  # @@protoc_insertion_point(class_scope:data_stream.DataResponse)
  })
_sym_db.RegisterMessage(DataResponse)

_DATASTREAM = DESCRIPTOR.services_by_name['DataStream']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATA._serialized_start=67
  _DATA._serialized_end=92
  _DATARESPONSE._serialized_start=94
  _DATARESPONSE._serialized_end=197
  _DATASTREAM._serialized_start=199
  _DATASTREAM._serialized_end=285
# @@protoc_insertion_point(module_scope)