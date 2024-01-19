from env import CONFIG
from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.collection import Collection

import col_type

mongodb_uri = "mongodb://%s:%s@%s:%s/%s?tls=%s" % (
    quote_plus(CONFIG.DATABASE.USER),
    quote_plus(CONFIG.DATABASE.PASSWORD),
    CONFIG.DATABASE.HOST,
    CONFIG.DATABASE.PORT,
    CONFIG.DATABASE.DB,
    repr(CONFIG.DATABASE.TLS).lower()
)

mongo_client = MongoClient(mongodb_uri)

DB = mongo_client[CONFIG.DATABASE.DB]

COL_ML: Collection[col_type.Message] = DB["message-log"]
COL_MDL: Collection[col_type.MessageDeleteLog] = DB["message-delete-log"]
COL_MEL: Collection[col_type.MessageEditLog] = DB["message-edit-log"]
COL_MCRL: Collection[col_type.MemberChangeRoleLog] = DB["member-change-role-log"]
COL_CEL: Collection[col_type.ClientErrorLog] = DB["client-error-log"]
COL_ACL: Collection[col_type.AppCommandLog] = DB["app-command-log"]
COL_MCL: Collection[col_type.MessageCommandLog] = DB["message-command-log"]
COL_D = DB["data"]
