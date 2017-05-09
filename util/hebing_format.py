# -*- coding: utf-8 -*-
from pymongo import MongoClient
import sys

raw_db_name = 'db_qikan'
raw_table_name = sys.argv[1]

new_db_name = 'db_qikan'
new_table_name = raw_table_name+'_clean'
client = MongoClient('dev.mongo.jscrapy.org', 27017)
db = client[raw_db_name]
new_db = client[new_db_name]

replace_field_name = ["book_name_zh", "book_name_en"]

for qk_name in replace_field_name:
    for u in db[raw_table_name].distinct(qk_name):
        dict_temp = dict()
        isSave = True
        for doc_to_combine in db[raw_table_name].find({qk_name: u}):  # 找到全部同名的
            if qk_name == 'book_name_en':  # 靠中文合并过的跳过
                bk_zh_name = doc_to_combine.get('book_name_zh')
                if bk_zh_name is not None and len(bk_zh_name) > 0:
                    isSave = False
                    break
            fen_lei = doc_to_combine.get('class')  # 'class'是个关键字，换成'fen_lei'
            if fen_lei:
                doc_to_combine['fen_lei'] = fen_lei

            dujia = doc_to_combine.get("is_du_jia")
            if dujia:
                doc_to_combine['is_du_jia'] = 'Y'
            else:
                doc_to_combine['is_du_jia'] = 'N'

            for (k, v) in doc_to_combine.items():
                if k is None or len(k) <= 0:
                    continue
                if v == '-' or v == '--':
                    continue

                if v == '停刊':
                    k = "status"
                if k == 'class' or k == '_form' or v is None or len(str(v)) == 0:  # 直接删除
                    continue
                if k == '_id':  # 替换id
                    dict_temp['raw_mongo_id'] = str(v)
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
                    elif v=='zazhi':
                        if dict_temp[k] != 'cnki' and dict_temp[k] != 'wanfang' and dict_temp[k]!='cqvip':
                            dict_temp[k] = v
                    continue
                if k == 'gmt_create' or k == '_id' or k == 'is_du_jia':  # 这三个字段无法len
                    continue
                elif v:
                    if len(v) > len(dict_temp.get(k)):
                        # print(" %s\t%s\t%s" % (k, dict_temp.get(k), v))
                        dict_temp[k] = v
                        # print(".")

        if isSave and len(dict_temp) > 0:
            # db.qikan_info.remove({"book_name_zh": u})
            new_db[new_table_name].insert(dict_temp)

    print(qk_name + " ok")
