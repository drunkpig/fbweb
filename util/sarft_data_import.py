# -*- coding=utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
db = client['db_qikan']
collection = db.qikan_info_clean

file_in_path = "C:\Work\Qikan\qikan_name_all_addinfo_fill.csv"
file_in = open(file_in_path, 'r')

filter_list = [u'', u'-', u'无', u'NULL', u'未知语言']

for line in file_in.readlines()[1:]:            # 从第二行开始读取
    line = line.decode('utf-8')
    QiKan_info_list = line.split(",")           # 按照逗号划分
    QiKan_cn = QiKan_info_list[2]              # 第三列为刊号 第一列刊名 第二列地址 第五列电话 第七列主管 第八列主办 第九列语种
    u = collection.find_one({"cn": QiKan_cn})
    if not u:
        u = collection.find_one({"cn": "CN" + QiKan_cn})
    if u:
        if QiKan_info_list[1] not in filter_list and len(QiKan_info_list[1]) > 6:  # 地址至少七个符号
            u["di_zhi"] = QiKan_info_list[1]
        if QiKan_info_list[4] not in filter_list and len(QiKan_info_list[4]) > 6:  # 至少七位号码
            u["dian_hua"] = QiKan_info_list[4]
        if len(QiKan_info_list) == 9:
            if QiKan_info_list[6] not in filter_list and len(QiKan_info_list[6]) > 2:  # 至少XX部
                u["zhu_guan_dan_wei"] = QiKan_info_list[6]
            if QiKan_info_list[7] not in filter_list and len(QiKan_info_list[7]) > 2:
                u["zhu_ban_dan_wei"] = QiKan_info_list[7]
            if QiKan_info_list[8] not in filter_list and len(QiKan_info_list[8]) > 1:
                u["yu_zhong"] = QiKan_info_list[8]
        collection.save(u)


