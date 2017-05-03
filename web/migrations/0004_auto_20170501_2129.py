# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-01 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_qikan__form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qikan',
            name='_from',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='数据来源'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='ban_mian_fei',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='版面费'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='ban_nian_jia',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='半年价'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='bian_geng',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='变更历史'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='ceng_yong_kan_ming',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='曾用刊名'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='chu_ban_di',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='出版地'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='chu_ban_ri_qi',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='chu_ban_she',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='chu_ban_zhou_qi',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='出版周期'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='chuang_kan_shi_jian',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='创刊时间'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='cn',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='CN'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='dan_jia',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='单价'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='di_zhi',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='dian_hua',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='ding_jia',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='定价'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='fa_bao_kan_ju',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='发报刊局'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='fa_xing_nian_fen',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='发行年份'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='feng_mian',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='fenlei',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='fu_he_ying_xiang_yin_zi',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='复合影响因子'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='gmt_create',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='gmt_create'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='guan_fang_wang_zhan',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='光方网站'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='guo_wai_shu_ju_ku_shou_lu',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='国外数据库收录'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='he_xin_lie_biao',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='核心列表'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='he_xin_list',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='核心列表'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='huo_jiang',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='获奖'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='is_du_jia',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='是否独家'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='is_he_xin',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='是否核心'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='is_you_xian_chu_ban',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='是否有限出版'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='issn',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='ISSN'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='jian_jie',
            field=models.CharField(blank=True, default='=暂无=', max_length=1000, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='kai_ben',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='开本'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='lan_mu',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='栏目'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='lu_yong_bi_li',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='录用比例'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='quan_nian_jia',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='全年价'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='shen_gao_fei',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='审稿费'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='shen_gao_su_du',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='审稿速度'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='shu_ju_ku_shou_lu',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='收录数据库'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='tou_gao_wang_zhan',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='投稿网站'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='url',
            field=models.CharField(blank=True, default='=暂无=', max_length=1000, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='xian_yong_kan_ming',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='现用刊名'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='you_fa_bian_hao',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='邮发编号'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='you_fa_dai_hao',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='邮发代号'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='you_xiang',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='you_zheng_bian_ma',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='邮政编码'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='yu_zhong',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='语种'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='zhu_ban_dan_wei',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='主办单位'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='zhu_bian',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='主编'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='zhu_guan_dan_wei',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='主管单位'),
        ),
        migrations.AlterField(
            model_name='qikan',
            name='zong_he_ying_xiang_yin_zi',
            field=models.CharField(blank=True, default='=暂无=', max_length=100, null=True, verbose_name='综合影响因子'),
        ),
    ]
