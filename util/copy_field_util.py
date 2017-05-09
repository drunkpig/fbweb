# -*- coding=utf-8 -*-
import sys
from pymongo import MongoClient

from_db = sys.argv[1]
from_table = sys.argv[2]

to_db = sys.argv[3]
to_table = sys.argv[4]

client = MongoClient("dev.mongo.jscrapy.org", 27017)
db = client[from_db]
from_table = db[from_table]
to_table = db[to_table]
field_to_copy = sys.argv[5]

for doc in to_table.find():  # 补充目的doc字段
    zh_name = doc.get('book_name_zh')
    en_name = doc.get('book_name_en')
    field_val = doc.get("fen_lei")
    if zh_name:
        copy_doc = from_table.find({"book_name_zh": zh_name})
        if copy_doc:
            for dc in copy_doc:
                val = dc.get("fen_lei")
                if val:
                    if val == '不限' or val == '-' or val == '--':
                        continue
                    else:
                        field_val = val
                        break
    elif en_name:
        copy_doc = from_table.find({"book_name_en": zh_name})
        if copy_doc:
            for dc in copy_doc:
                val = dc.get("fen_lei")
                if val:
                    if val=='不限' or val=='-' or val=='--':
                        continue
                    else:
                        field_val = val
                        break
    else:
        print("find no book: %s\t%s" % (zh_name, en_name))
        continue

    doc[field_to_copy] = field_val
    to_table.save(doc)
