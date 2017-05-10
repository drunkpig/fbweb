from fbweb import settings
import sys
from os.path import dirname
from pymongo import MongoClient
from django.core.cache import cache

"""
[
{"文件名字，包含了要bit位编码的字段列表": 一个数字，包含了在bit位串中占据的位数}
]
"""
field_file = [
    {"chu_ban_zhou_qi.log": [5, "出版周期"]},
    {"jian_kan_shi_jian.log": [3, "见刊时间"]},
    {"chu_ban_sheng_fen.log": [6, "省份"]},
    {"kuai_jie_fen_lei.log": [6, "快捷分类"]}
]

encode_field_result = {}  # 存储最终的结果
tag_name_zh = {}
bit_op_map = {}


def init_data():
    all_file_list = []
    all_bit_op_count = []
    temp = []
    for doc in field_file:
        for k, v in doc.items():
            temp.append(v[0])
            tag_name_zh[k.split(".")[0]] = v[1]
            all_file_list.append(k)

    for i in range(0, len(temp)):
        m = 0
        for j in range(0, i):
            m += temp[j]
        tp = (temp[i], m, (2 ** (temp[i]) - 1) << m)
        all_bit_op_count.append(tp)
        km = all_file_list[i].split(".")[0]
        bit_op_map[km] = tp

    bit_wise_index = 0
    for file in all_file_list:  # 分别打开每个文件对文件进行编码
        result = {}
        logdir = dirname(__file__)
        f = open(logdir + "/" + file, "r")

        field_list = ['不限'] + f.readlines()
        bit_wise = all_bit_op_count[bit_wise_index][1]  # 右移多少位
        for code in range(0, len(field_list)):
            fd = field_list[code].strip()
            encode = (code) << bit_wise  # code+1是为了把全0留出来当做‘无限’这个条件
            result[fd] = encode
            # print("%s\t%s" % (fd, str(bin(encode))))
        bit_wise_index += 1
        encode_field_result[file.split(".")[0]] = result


def get_bit_op_wise():
    dt = cache.get("bit_op_map")
    if not dt:
        init_data()
        cache.set("bit_op_map", bit_op_map, 300)

    return bit_op_map;


def get_encode_field_result():
    dt = cache.get("encode_field_result")
    if not dt:
        init_data()
        cache.set("encode_field_result", encode_field_result, 300)
    return encode_field_result;


def get_tag_name_zh():
    dt = cache.get("tag_name_zh")
    if not dt:
        init_data()
        cache.set("tag_name_zh", tag_name_zh, 300)
    return tag_name_zh;


def do_sync():
    client = MongoClient("dev.mongo.jscrapy.org", 27017)
    db = client['db_qikan']
    collection = sys.argv[1]
    encode_field_result1 = get_encode_field_result();

    for doc in db[collection].find():
        doc['s_code'] = 0  # 初始化编码
        for k, v in encode_field_result1.items():
            field_name = k
            encode_dic = v
            field_value = doc.get(field_name)
            if field_value:
                scode = encode_dic.get(field_value)
                doc['s_code'] = doc['s_code'] | scode

        print(doc['s_code'])
        db[collection].save(doc)


if __name__ == "__main__":
    do_sync()
