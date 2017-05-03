# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient

client = MongoClient('dev.mongo.jscrapy.org', 27018)
db = client['db_qikan']

client = MongoClient("dev.mongo.jscrapy.org", 27017)
new_db = client['db_qikan']

replace_field_name = ["book_name_zh", "book_name_en"]

for qk_name in replace_field_name:
    for u in db.qikan_info.distinct(qk_name):
        dict_temp = dict()
        count_info = 0
        for doc_to_combine in db.qikan_info.find({qk_name: u}):  # 找到全部同名的
            count_info += 1

            for (k, v) in doc_to_combine.items():
                if qk_name == 'book_name_en':  # 靠中文合并过的跳过
                    if k == 'book_name_zh' and v is not None and len(v) > 0:
                        continue
                if v == '停刊':
                    k = "status"
                if k == '_form' or v is None or len(str(v)) == 0:  # 直接删除
                    continue
                if k == '_id':  # 替换id
                    dict_temp['raw_mongo_id'] = v
                    continue
                if not dict_temp.get(k):
                    dict_temp[k] = v
                    # print("set %s = %s" % (k, v))
                    continue
                if k == '_from':  # 来源
                    if v == 'cnki':
                        dict_temp[k] = v
                    elif v == 'wanfang':
                        if dict_temp[k] != 'cnki':
                            dict_temp[k] = v
                    elif v == 'cqvip':
                        if dict_temp[k] != 'cnki' and dict_temp[k] != 'wanfang':
                            dict_temp[k] = v
                    continue
                if k == 'gmt_create' or k == '_id' or k == 'is_du_jia':  # 这三个字段无法len
                    continue
                elif v:
                    if len(v) > len(dict_temp.get(k)):
                        # print(" %s\t%s\t%s" % (k, dict_temp.get(k), v))
                        dict_temp[k] = v
                        # print(".")

        if count_info > 0:
            # db.qikan_info.remove({"book_name_zh": u})
            new_db.qikan_info_new1.insert(dict_temp)

    print(qk_name + "ok")
