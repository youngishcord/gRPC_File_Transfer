# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x07message\"0\n\x0f\x43ommandsRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0b\n\x03md5\x18\x02 \x01(\t\" \n\rCommandsReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x11\x46ileUploadRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"#\n\x10\x46ileSuccessReply\x12\x0f\n\x07success\x18\x01 \x01(\t2\x92\x01\n\x07Message\x12\x42\n\x0e\x43ommandMessage\x12\x18.message.CommandsRequest\x1a\x16.message.CommandsReply\x12\x43\n\nUploadFile\x12\x1a.message.FileUploadRequest\x1a\x19.message.FileSuccessReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMANDSREQUEST._serialized_start=27
  _COMMANDSREQUEST._serialized_end=75
  _COMMANDSREPLY._serialized_start=77
  _COMMANDSREPLY._serialized_end=109
  _FILEUPLOADREQUEST._serialized_start=111
  _FILEUPLOADREQUEST._serialized_end=144
  _FILESUCCESSREPLY._serialized_start=146
  _FILESUCCESSREPLY._serialized_end=181
  _MESSAGE._serialized_start=184
  _MESSAGE._serialized_end=330
# @@protoc_insertion_point(module_scope)