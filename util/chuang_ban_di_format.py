# -*- coding=utf-8 -*-
import sys
from pymongo import MongoClient

client = MongoClient("dev.mongo.jscrapy.org", 27017)
db = client['db_qikan']
collection = sys.argv[1]

for doc_all in db[collection].find():
    if doc_all.get("chu_ban_di"):
        text = doc_all["chu_ban_di"]
        if '省' in text:
            curs_i = text.index(u'省')
            doc_all["chu_ban_sheng_fen"] = text[0:curs_i]
            doc_all["chu_ban_di"] = text[curs_i+1:-1]
            db[collection].save(doc_all)
            print("/", end="")
        elif u'自治区' in text:
                curs_i = text.index(u'区')
                doc_all["chu_ban_sheng_fen"] = text[0:curs_i-2]
                doc_all["chu_ban_di"] = text[curs_i+1:-1]
                db[collection].save(doc_all)
                print("\\", end="")
        elif not text:
            print("add default pls")













#for u in db.qikan_info.find({"chu_ban_di": {{'$regex': "$exists:true"}}}): # 找到存在出版地字段
        #if u'\u4e00' <= text[0] <= u'\u9fa5': #是否是中文

