# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: Request.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'Request.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rRequest.proto\"&\n\x08\x45xtValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x94\x04\n\x07Request\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x13\n\x0bsequence_id\x18\x02 \x01(\x03\x12\x13\n\x0bsdk_version\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\t\x12\r\n\x05refer\x18\x05 \x01(\x05\x12\x12\n\ninbox_type\x18\x06 \x01(\x03\x12\x14\n\x0c\x62uild_number\x18\x07 \x01(\t\x12\x1a\n\x04\x62ody\x18\x08 \x01(\x0b\x32\x0c.RequestBody\x12\x11\n\tdevice_id\x18\t \x01(\t\x12\x0f\n\x07\x63hannel\x18\n \x01(\t\x12\x17\n\x0f\x64\x65vice_platform\x18\x0b \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x0c \x01(\t\x12\x12\n\nos_version\x18\r \x01(\t\x12\x14\n\x0cversion_code\x18\x0e \x01(\t\x12&\n\x07headers\x18\x0f \x03(\x0b\x32\x15.Request.HeadersEntry\x12\x11\n\tconfig_id\x18\x10 \x01(\x05\x12\x1e\n\ntoken_info\x18\x11 \x01(\x0b\x32\n.TokenInfo\x12\x11\n\tauth_type\x18\x12 \x01(\x05\x12\x0b\n\x03\x62iz\x18\x15 \x01(\t\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x16 \x01(\t\x12\x0f\n\x07ts_sign\x18\x17 \x01(\t\x12\x10\n\x08sdk_cert\x18\x18 \x01(\t\x12\x14\n\x0creuqest_sign\x18\x19 \x01(\t\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xeb\x01\n\x0bRequestBody\x12\x34\n\x11send_message_body\x18\x64 \x01(\x0b\x32\x17.SendMessageRequestBodyH\x00\x12H\n\x1b\x63reate_conversation_v2_body\x18\xe1\x04 \x01(\x0b\x32 .CreateConversationV2RequestBodyH\x00\x12T\n\"get_conversation_info_list_v2_body\x18\xe2\x04 \x01(\x0b\x32%.GetConversationInfoListV2RequestBodyH\x00\x42\x06\n\x04\x62ody\"\xb8\x02\n\x16SendMessageRequestBody\x12\x17\n\x0f\x63onversation_id\x18\x01 \x01(\t\x12\x19\n\x11\x63onversation_type\x18\x02 \x01(\x05\x12\x1d\n\x15\x63onversation_short_id\x18\x03 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x16\n\x03\x65xt\x18\x05 \x03(\x0b\x32\t.ExtValue\x12\x14\n\x0cmessage_type\x18\x06 \x01(\x05\x12\x0e\n\x06ticket\x18\x07 \x01(\t\x12\x19\n\x11\x63lient_message_id\x18\x08 \x01(\t\x12\x17\n\x0fmentioned_users\x18\t \x03(\x03\x12\x1a\n\x12ignore_badge_count\x18\n \x01(\x08\x12,\n\x0cref_msg_info\x18\x0b \x01(\x0b\x32\x16.ReferencedMessageInfo\"y\n\x15ReferencedMessageInfo\x12\x1b\n\x13original_message_id\x18\x01 \x01(\x03\x12\x1f\n\x17original_message_sender\x18\x02 \x01(\t\x12\"\n\x1aoriginal_message_timestamp\x18\x03 \x01(\x03\"^\n\tTokenInfo\x12\x0f\n\x07mark_id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\x05\x12\x0f\n\x07user_id\x18\x04 \x01(\x03\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\"\xa2\x02\n\x1f\x43reateConversationV2RequestBody\x12\x19\n\x11\x63onversation_type\x18\x01 \x01(\x05\x12\x14\n\x0cparticipants\x18\x02 \x03(\x03\x12\x12\n\npersistent\x18\x03 \x01(\x08\x12\x15\n\ridempotent_id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x12\n\navatar_url\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12=\n\x07\x62iz_ext\x18\x08 \x03(\x0b\x32,.CreateConversationV2RequestBody.BizExtEntry\x1a-\n\x0b\x42izExtEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"`\n$GetConversationInfoListV2RequestBody\x12\x38\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32*.GetConversationInfoListV2ResponseBodyData\"~\n)GetConversationInfoListV2ResponseBodyData\x12\x17\n\x0f\x63onversation_id\x18\x01 \x01(\t\x12\x1d\n\x15\x63onversation_short_id\x18\x02 \x01(\x03\x12\x19\n\x11\x63onversation_type\x18\x03 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUEST_HEADERSENTRY']._loaded_options = None
  _globals['_REQUEST_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_CREATECONVERSATIONV2REQUESTBODY_BIZEXTENTRY']._loaded_options = None
  _globals['_CREATECONVERSATIONV2REQUESTBODY_BIZEXTENTRY']._serialized_options = b'8\001'
  _globals['_EXTVALUE']._serialized_start=17
  _globals['_EXTVALUE']._serialized_end=55
  _globals['_REQUEST']._serialized_start=58
  _globals['_REQUEST']._serialized_end=590
  _globals['_REQUEST_HEADERSENTRY']._serialized_start=544
  _globals['_REQUEST_HEADERSENTRY']._serialized_end=590
  _globals['_REQUESTBODY']._serialized_start=593
  _globals['_REQUESTBODY']._serialized_end=828
  _globals['_SENDMESSAGEREQUESTBODY']._serialized_start=831
  _globals['_SENDMESSAGEREQUESTBODY']._serialized_end=1143
  _globals['_REFERENCEDMESSAGEINFO']._serialized_start=1145
  _globals['_REFERENCEDMESSAGEINFO']._serialized_end=1266
  _globals['_TOKENINFO']._serialized_start=1268
  _globals['_TOKENINFO']._serialized_end=1362
  _globals['_CREATECONVERSATIONV2REQUESTBODY']._serialized_start=1365
  _globals['_CREATECONVERSATIONV2REQUESTBODY']._serialized_end=1655
  _globals['_CREATECONVERSATIONV2REQUESTBODY_BIZEXTENTRY']._serialized_start=1610
  _globals['_CREATECONVERSATIONV2REQUESTBODY_BIZEXTENTRY']._serialized_end=1655
  _globals['_GETCONVERSATIONINFOLISTV2REQUESTBODY']._serialized_start=1657
  _globals['_GETCONVERSATIONINFOLISTV2REQUESTBODY']._serialized_end=1753
  _globals['_GETCONVERSATIONINFOLISTV2RESPONSEBODYDATA']._serialized_start=1755
  _globals['_GETCONVERSATIONINFOLISTV2RESPONSEBODYDATA']._serialized_end=1881
# @@protoc_insertion_point(module_scope)
