# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: alvenir_grpc_contracts/summary/v1/analytics.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'alvenir_grpc_contracts/summary/v1/analytics.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alvenir_grpc_contracts.types.v1 import status_pb2 as alvenir__grpc__contracts_dot_types_dot_v1_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1alvenir_grpc_contracts/summary/v1/analytics.proto\x12!alvenir_grpc_contracts.summary.v1\x1a,alvenir_grpc_contracts/types/v1/status.proto\"d\n\x1bPostSummaryAnalyticsRequest\x12\x0f\n\x07\x63\x61ll_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65\x64ited_summary\x18\x02 \x01(\t\x12\x1c\n\x14wrap_up_time_seconds\x18\x03 \x01(\x02\"p\n\x1cPostSummaryAnalyticsResponse\x12?\n\x06status\x18\x02 \x01(\x0e\x32/.alvenir_grpc_contracts.types.v1.ResponseStatus\x12\x0f\n\x07message\x18\x01 \x01(\t2\xae\x01\n\x10\x41nalyticsService\x12\x99\x01\n\x14PostSummaryAnalytics\x12>.alvenir_grpc_contracts.summary.v1.PostSummaryAnalyticsRequest\x1a?.alvenir_grpc_contracts.summary.v1.PostSummaryAnalyticsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'alvenir_grpc_contracts.summary.v1.analytics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_POSTSUMMARYANALYTICSREQUEST']._serialized_start=134
  _globals['_POSTSUMMARYANALYTICSREQUEST']._serialized_end=234
  _globals['_POSTSUMMARYANALYTICSRESPONSE']._serialized_start=236
  _globals['_POSTSUMMARYANALYTICSRESPONSE']._serialized_end=348
  _globals['_ANALYTICSSERVICE']._serialized_start=351
  _globals['_ANALYTICSSERVICE']._serialized_end=525
# @@protoc_insertion_point(module_scope)
