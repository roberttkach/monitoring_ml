# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pre-processing.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pre-processing.proto\"6\n\x05Image\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nimage_data\x18\x02 \x01(\x0c\x12\r\n\x05label\x18\x03 \x01(\x05\"$\n\nImageBatch\x12\x16\n\x06images\x18\x01 \x03(\x0b\x32\x06.Imageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pre_processing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGE']._serialized_start=24
  _globals['_IMAGE']._serialized_end=78
  _globals['_IMAGEBATCH']._serialized_start=80
  _globals['_IMAGEBATCH']._serialized_end=116
# @@protoc_insertion_point(module_scope)
