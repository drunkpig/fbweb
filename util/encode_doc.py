from fbweb import settings
import sys
from pymongo import MongoClient

"""
[
{"文件名字，包含了要bit位编码的字段列表": 一个数字，包含了在bit位串中占据的位数}
]
"""
field_file = [
    {"chu_ban_zhou_qi.log": 5},
    {"jian_kan_shi_jian.log": 3},
    {"chu_ban_sheng_fen.log": 6}
]

encode_field_result = {}  # 存储最终的结果

all_file_list = []
all_bit_op_count = []
temp = []
for doc in field_file:
    for k, v in doc.items():
        temp.append(v)
        all_file_list.append(k)

for i in range(0, len(temp)):
    m = 0
    for j in range(0, i):
        m += temp[j]
    all_bit_op_count.append(m)

bit_wise_index = 0
for file in all_file_list:  # 分别打开每个文件对文件进行编码
    result = {}
    f = open(file, "r")
    field_list = f.readlines()
    bit_wise = all_bit_op_count[bit_wise_index]  # 右移多少位
    for code in range(0, len(field_list)):
        fd = field_list[code].strip()
        encode = (code + 1) << bit_wise  # code+1是为了把全0留出来当做‘无限’这个条件
        result[fd] = encode
        print("%s\t%s" % (fd, str(bin(encode))))
    bit_wise_index += 1
    encode_field_result[file.split(".")[0]] = result
    print("==============================")

client = MongoClient("dev.mongo.jscrapy.org", 27017)
db = client['db_qikan']
collection = sys.argv[1]

for doc in db[collection].find():
    doc['s_code'] = 0  # 初始化编码
    for k, v in encode_field_result.items():
        field_name = k
        encode_dic = v
        field_value = doc.get(field_name)
        if field_value:
            scode = encode_dic.get(field_value)
            doc['s_code'] = doc['s_code'] | scode

    # print(doc['s_code'])
    db[collection].save(doc)
