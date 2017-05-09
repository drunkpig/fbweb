from pymongo import MongoClient
from math import ceil
import sys

db_name = sys.argv[1]
collection_name = sys.argv[2]

client = MongoClient("dev.mongo.jscrapy.org", 27017)
db = client[db_name]
collection = db[collection_name]

qikan_docs = collection.find()

field_len_dic = {}     # field_name:max(len)
for doc in qikan_docs:
    for k, v in doc.items():
        len_exists = field_len_dic.get(k)
        new_len = len(str(v))
        if len_exists:
            if new_len>len_exists:
                field_len_dic[k] = new_len
        else:
            field_len_dic[k] = new_len

print(field_len_dic)