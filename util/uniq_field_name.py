"""
输出一个db， collection, 输出里面全部的字段key值（去重之后）
"""
from pymongo import MongoClient
from math import ceil
import sys

db_name = sys.argv[1]
collection_name = sys.argv[2]

client = MongoClient("dev.mongo.jscrapy.org", 27017)
db = client[db_name]
collection = db[collection_name]
doc_count = collection.count()  # 总共多少文档
batch_size = 100
page_count = ceil(doc_count / batch_size)  # 计算出一共多少页
cur_batch = 0

key_set = []
#f = open(field_export + ".log", "w", encoding="utf-8")

for i in range(0, page_count):
    qikan_docs = collection.find().skip(cur_batch * batch_size).limit(batch_size)
    # 插入default RDBM
    for doc in qikan_docs:
        keys = doc.keys()
        key_set += keys;

    cur_batch += 1


for i in set(key_set):
    print(i)

exit()

