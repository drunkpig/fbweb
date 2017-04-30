# Create your models here.
from django.db import models
from multiselectfield import MultiSelectField


class Qikan(models.Model):
    doc_id = models.CharField("期刊DocID", max_length=100)
    book_name_zh = models.CharField("期刊中文名称", max_length=100, blank=True, null=True, default="=暂无=")
    book_name_en = models.CharField("期刊英文名称", max_length=100, blank=True, null=True, default="=暂无=")

    def __str__(self):
        title = self.book_name_zh
        if title is None:
            title = self.book_name_en
        return title


# 价格 编辑 编辑QQ 编辑电话 收录网站 版面字数 级别
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
