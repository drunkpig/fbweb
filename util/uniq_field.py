from pymongo import MongoClient
from math import ceil
import sys


field_export = sys.argv[1]

client = MongoClient("dev.mongo.jscrapy.org", 27018)
db = client.db_qikan
collection = db.qikan_info
doc_count = collection.count()  # 总共多少文档
batch_size = 100
page_count = ceil(doc_count / batch_size)  # 计算出一共多少页
cur_batch = 0
ct = 0;
value_set = set()
#f = open(field_export + ".log", "w", encoding="utf-8")

for i in range(0, page_count):
    qikan_docs = collection.find().skip(cur_batch * batch_size).limit(batch_size)
    # 插入default RDBM
    for doc in qikan_docs:
        field_value = doc.get(field_export)
        if field_value:
            arr = field_value.split("#")
            for v in arr:
                value_set.add(v)
                #print(v, end="\n")
                #f.write(v+"\n")
        ct += 1
    cur_batch += 1

for i in value_set:
    print(i, end="\n")

exit()
