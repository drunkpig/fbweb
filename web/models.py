# Create your models here.
from django.db import models
from multiselectfield import MultiSelectField

from bitfield import BitField
max_len = {
    "ding_jia":7,
    "jian_kan_shi_jian":6,
    "book_name_zh":94,
    "book_name_en":157,
    "jian_jie":3680,
    "feng_mian":3992975,
    "s_code":6,
    "ji_du_jia":6,
    "bian_geng":151,
    "shen_gao_su_du":18,
    "is_du_jia":1,
    "ceng_yong_kan_ming":430,
    "chu_ban_she":22,
    "you_fa_dai_hao":20,
    "shu_ju_ku_shou_lu":221,
    "is_he_xin":1,
    "_from":8,
    "dian_hua":49,
    "chuang_kan_shi_jian":10,
    "chu_ban_sheng_fen":3,
    "url":546,
    "dan_jia":6,
    "fa_bao_kan_ju":10,
    "_id":24,
    "fen_lei":39,
    "cn":12,
    "qi_kan_ji_bie":34,
    "lan_mu":986,
    "duan_jian_jie":200,
    "zhu_guan_dan_wei":50,
    "huo_jiang":568,
    "chu_ban_zhou_qi":5,
    "kuai_jie_fen_lei":3,
    "issn":30,
    "zhu_ban_dan_wei":104,
    "zhu_bian":25,
    "he_xin_list":77,
    "raw_mongo_id":24,
    "lu_yong_bi_li":4,
    "zong_he_ying_xiang_yin_zi":6,
    "chu_ban_di":186,
    "gmt_create":26,
    "tou_gao_wang_zhan":219,
    "you_zheng_bian_ma":12,
    "fu_he_ying_xiang_yin_zi":5,
    "kai_ben":5,
    "ban_nian_jia":6,
    "you_fa_bian_hao":7,
    "fa_xing_nian_fen":4,
    "yu_zhong":6,
    "guo_wai_shu_ju_ku_shou_lu":224,
    "guan_fang_wang_zhan":255,
    "xiang_guan_lian_jie":1853,
    "he_xin_lie_biao":89,
    "xian_yong_kan_ming":75,
    "za_zhi_she_jie_shao":9563,
    "isbn":23,
    "you_xiang":217,
    "shen_gao_fei":12,
    "is_you_xian_chu_ban":1,
    "status":2,
    "di_zhi":61,
    "ban_mian_fei":12,
    "quan_nian_jia":9
}

# for k, v in max_len.items():
#     max_len[k] = v+8

class Qikan(models.Model):
    doc_id = models.CharField("期刊DocID", max_length=50)
    book_name_zh = models.CharField("期刊中文名称", max_length=max_len['book_name_zh'], blank=True, null=True, default="-")
    book_name_en = models.CharField("期刊英文名称", max_length=max_len['book_name_en'], blank=True, null=True, default="-")
    ji_du_jia = models.CharField("季度价格", max_length=max_len['ji_du_jia'], blank=True, null=True, default="-")
    cn = models.TextField("CN", max_length=max_len['cn'], blank=True, null=True, default="-")
    you_fa_bian_hao = models.CharField("邮发编号", max_length=max_len['you_fa_bian_hao'], blank=True, null=True, default="-")
    quan_nian_jia = models.CharField("全年价", max_length=max_len['quan_nian_jia'], blank=True, null=True, default="-")
    chu_ban_zhou_qi = models.CharField("出版周期", max_length=max_len['chu_ban_zhou_qi'], blank=True, null=True, default="-")
    feng_mian = models.TextField("封面", blank=True, null=True, default="-")
    fa_xing_nian_fen = models.CharField("发行年份", max_length=max_len['fa_xing_nian_fen'], blank=True, null=True, default="-")
    ban_nian_jia = models.CharField("半年价", max_length=max_len['ban_nian_jia'], blank=True, null=True, default="-")
    fa_bao_kan_ju = models.CharField("发报刊局", max_length=max_len['fa_bao_kan_ju'], blank=True, null=True, default="-")
    #chu_ban_ri_qi = models.CharField("出版日期", max_length=max_len['chu_ban_ri_qi'], blank=True, null=True, default="-")
    jian_jie = models.TextField("简介", blank=True, null=True, default="-")
    url = models.CharField("URL", max_length=max_len['url'], blank=True, null=True, default="-")
    dan_jia = models.CharField("单价", max_length=max_len['dan_jia'], blank=True, null=True, default="-")
    lan_mu = models.TextField("栏目", blank=True, null=True, default="-")
    _from = models.CharField("数据来源", max_length=max_len['_from'], blank=True, null=True, default="-")
    chu_ban_she = models.CharField("出版社", max_length=max_len['chu_ban_she'], blank=True, null=True, default="-")
    fen_lei = models.CharField("分类", max_length=max_len['fen_lei'], blank=True, null=True, default="-")
    you_xiang = models.CharField("邮箱", max_length=max_len['you_xiang'], blank=True, null=True, default="-")
    huo_jiang = models.TextField("获奖", blank=True, null=True, default="-")
    you_zheng_bian_ma = models.CharField("邮政编码", max_length=max_len['you_zheng_bian_ma'], blank=True, null=True, default="-")
    zhu_ban_dan_wei = models.CharField("主办单位", max_length=max_len['zhu_ban_dan_wei'], blank=True, null=True, default="-")
    dian_hua = models.CharField("电话", max_length=max_len['dian_hua'], blank=True, null=True, default="-")
    zhu_bian = models.CharField("主编", max_length=max_len['zhu_bian'], blank=True, null=True, default="-")
    guan_fang_wang_zhan = models.CharField("官方网站", max_length=max_len['guan_fang_wang_zhan'], blank=True, null=True, default="-")
    is_you_xian_chu_ban = models.CharField("是否有限出版", max_length=max_len['is_you_xian_chu_ban'], blank=True, null=True, default="-")
    is_he_xin = models.CharField("是否核心", max_length=max_len['is_he_xin'], blank=True, null=True, default="-")
    di_zhi = models.CharField("地址", max_length=max_len['di_zhi'], blank=True, null=True, default="-")
    issn = models.CharField("ISSN", max_length=max_len['issn'], blank=True, null=True, default="-")
    zhu_guan_dan_wei = models.CharField("主管单位", max_length=max_len['zhu_guan_dan_wei'], blank=True, null=True, default="-")
    xian_yong_kan_ming = models.CharField("现用刊名", max_length=max_len['xian_yong_kan_ming'], blank=True, null=True, default="-")
    you_fa_dai_hao = models.CharField("邮发代号", max_length=max_len['you_fa_dai_hao'], blank=True, null=True, default="-")
    is_du_jia = models.CharField("是否独家", max_length=max_len['is_du_jia'], blank=True, null=True, default="-")
    he_xin_list = models.TextField("核心列表", blank=True, null=True, default="-")
    chu_ban_di = models.CharField("出版地", max_length=max_len['chu_ban_di'], blank=True, null=True, default="-")
    chuang_kan_shi_jian = models.CharField("创刊时间", max_length=max_len['chuang_kan_shi_jian'], blank=True, null=True, default="-")
    zong_he_ying_xiang_yin_zi = models.CharField("综合影响因子", max_length=max_len['zong_he_ying_xiang_yin_zi'], blank=True, null=True, default="-")
    kai_ben = models.CharField("开本", max_length=max_len['kai_ben'], blank=True, null=True, default="-")
    fu_he_ying_xiang_yin_zi = models.CharField("复合影响因子", max_length=max_len['fu_he_ying_xiang_yin_zi'], blank=True, null=True, default="-")
    ceng_yong_kan_ming = models.TextField("曾用刊名", blank=True, null=True, default="-")
    shu_ju_ku_shou_lu = models.CharField("收录数据库", max_length=max_len['shu_ju_ku_shou_lu'], blank=True, null=True, default="-")
    yu_zhong = models.CharField("语种", max_length=max_len['yu_zhong'], blank=True, null=True, default="-")
    ding_jia = models.CharField("定价", max_length=max_len['ding_jia'], blank=True, null=True, default="-")
    bian_geng = models.CharField("变更历史", max_length=max_len['bian_geng'], blank=True, null=True, default="-")
    he_xin_lie_biao = models.CharField("核心列表", max_length=max_len['he_xin_lie_biao'], blank=True, null=True, default="-")
    guo_wai_shu_ju_ku_shou_lu = models.CharField("国外数据库收录", max_length=max_len['guo_wai_shu_ju_ku_shou_lu'], blank=True, null=True, default="-")
    ban_mian_fei = models.CharField("版面费", max_length=max_len['ban_mian_fei'], blank=True, null=True, default="-")
    tou_gao_wang_zhan = models.CharField("投稿网站", max_length=max_len['tou_gao_wang_zhan'], blank=True, null=True, default="-")
    shen_gao_su_du = models.CharField("审稿速度", max_length=max_len['shen_gao_su_du'], blank=True, null=True, default="-")
    lu_yong_bi_li = models.CharField("录用比例", max_length=max_len['lu_yong_bi_li'], blank=True, null=True, default="-")
    shen_gao_fei = models.CharField("审稿费", max_length=max_len['shen_gao_fei'], blank=True, null=True, default="-")
    chu_ban_sheng_fen = models.CharField("出版省份", max_length=max_len['chu_ban_sheng_fen'], blank=True, null=True, default="-")
    duan_jian_jie = models.TextField("简介", blank=True, null=True, default="-")
    isbn = models.CharField("ISBN", max_length=max_len['isbn'], blank=True, null=True, default="-")
    jian_kan_shi_jian = models.CharField("见刊时间", max_length=max_len['jian_kan_shi_jian'], blank=True, null=True, default="-")
    kuai_jie_fen_lei = models.CharField("快捷分类", max_length=max_len['kuai_jie_fen_lei'], blank=True, null=True, default="-")
    qi_kan_ji_bie = models.CharField("期刊级别", max_length=max_len['qi_kan_ji_bie'], blank=True, null=True, default="-")
    status = models.CharField("发行状态", max_length=max_len['status'], blank=True, null=True, default="-")
    xiang_guan_lian_jie = models.CharField("相关链接", max_length=max_len['xiang_guan_lian_jie'], blank=True, null=True, default="-")
    za_zhi_she_jie_shao = models.TextField("杂志社介绍",  blank=True, null=True, default="-")
    s_code = models.BigIntegerField()

def __str__(self):
    title = self.book_name_zh
    if title is None:
        title = self.book_name_en
    return title  # 价格 编辑 编辑QQ 编辑电话 收录网站 版面字数 级别
class Price(models.Model):
    price = models.DecimalField("价格", max_digits=7, decimal_places=5)
    bianji = models.CharField("编辑名字", max_length=20, null=True)
    qq = models.CharField('QQ号', max_length=15)
    tel = models.CharField('联系电话', max_length=15)
    site_collected = MultiSelectField("收录网站", max_choices=5,
                                      choices=(
                                          ("知网", '知网'),
                                          ("万方", '万方'),
                                          ("CQVIP", 'CQVIP'),
                                          ("龙源", '龙源'),
                                      )
                                      )
    words_per_article = models.IntegerField("版面字数")
    level = models.CharField("刊物级别", max_length=100, choices=(("省级", "省级"), ("国家级", "国家级"), ("默认", "默认")))  # 省级、国家级..

    qikan = models.ForeignKey(Qikan, related_name="刊物报价")
