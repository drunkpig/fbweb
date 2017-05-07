# -*- coding=utf-8 -*-
import sys
from pymongo import MongoClient

map = {
    "双月刊": "双月刊",
    "Tri-annual": "三年刊",
    "Biweekly": "双周刊",
    "旬刊": "旬刊",
    "旬报": "旬刊",
    "季刊": "季刊",
    "不定": "不定期",
    "不定期": "不定期",
    "Irregular": "不定期",
    "月刊": "月刊",
    "Monthly": "月刊",
    "月度刊":"月刊",
    "双周刊": "双周刊",
    "半月刊": "半月刊",
    "半月报": "半月刊",
    "半年": "半年刊",
    "半年刊": "半年刊",
    "Quarterly": "季刊",
    "双月": "双月刊",
    "Weekly": "周刊",
    "月报": "月刊",

    "Bimonthly": "双月刊",

    "Annual": "年刊",
    "半月": "半月刊",
    "一周两刊": "一周两刊",
    "一周两报": "一周两刊",
    "日报": "日刊",
    "双周报": "双周刊",
    "周报": "周刊",
    "周刊": "周刊",
    "四月一期": "四月一刊",
    "年刊": "年刊",
    "全年刊": "年刊",

    "年3期": "一年3期",
    "年5期": "一年5期",
    "年7期": "一年7期",
    "年10期": "一年10期",
    "年13期": "一年13期",
    "年48期": "一年48期",
    "年50期": "一年50期",
    "年53期": "一年53期",
    "年72期": "一年72期",

    "周二刊": "周刊",
    "一旬两报": "一旬2刊",
    "一周三报": "一周3刊",
    "一周四报": "一周4刊",
    "一周五报": "一周5刊",
    "一周六报": "一周6刊",
    "Semimonthly": "半月刊",
    "Semiannual": "半年刊",

}
client = MongoClient("dev.mongo.jscrapy.org", 27017)
db = client['db_qikan']
collection = sys.argv[1]

for doc_all in db[collection].find():
    if doc_all.get("chu_ban_zhou_qi"):
        text = doc_all["chu_ban_zhou_qi"]
        if not text:
            doc_all['chu_ban_zhou_qi'] = map['不定期']

        else:
            val = doc_all['chu_ban_zhou_qi']
            replace_val = map.get(val.strip())
            if replace_val:
                doc_all['chu_ban_zhou_qi'] = replace_val
    db[collection].save(doc_all)

exit
