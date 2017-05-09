from util.encode_doc import do_sync
from util.encode_doc import get_bit_op_wise
from util.encode_doc import get_encode_field_result
from util.encode_doc import get_tag_name_zh


def get_seg_list(search_code):
    """

    :return:
    """
    bit_wise_array = get_bit_op_wise()
    field_encode_map = get_encode_field_result()
    tag_zh = get_tag_name_zh()
    seg_map = {}  # 结果
    for k, v in field_encode_map.items():
        seg_map[k] = {}

    for k, v in field_encode_map.items():
        for m, n in v.items():
            seg_map[k][m] = (n, False)

    # 通过bit位移和search_code计算tag实际link参数

    pass


get_seg_list(0)
