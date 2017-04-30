# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId
from math import ceil
from .models import Qikan


def index(request):
    item_per_page = settings.ITEM_PER_PAGE
    start_page = 0;
    return render(request, "web/index.html", get_docs(start_page, item_per_page))


def list(request, start_page):
    start_page = int(start_page)
    if start_page < 0:
        start_page = 0
    item_per_page = settings.ITEM_PER_PAGE

    return render(request, "web/index.html", get_docs(start_page, item_per_page))


def sync_mongo(request):
    """
    把mongodb里的settings.SYNC_FIELDS同步到default db
    :param request:
    :return:
    """
    field_config = settings.QIKAN_FIELD_ZH_NAME
    client = MongoClient(settings.QIKAN_DATABASES['HOST'], settings.QIKAN_DATABASES['PORT'])
    db = client.db_qikan
    collection = db.qikan_info
    doc_count = collection.count()  # 总共多少文档
    batch_size = 100
    page_count = ceil(doc_count / batch_size)  # 计算出一共多少页
    cur_batch = 0
    ct = 0;
    for i in range(0, page_count):
        qikan_docs = collection.find().skip(cur_batch * batch_size).limit(batch_size)
        # 插入default RDBM
        for doc in qikan_docs:
            qikan = Qikan()
            doc_id = str(doc['_id'])
            name_zh = doc.get('book_name_zh')
            name_en = doc.get('book_name_en')
            Qikan.objects.update_or_create({"doc_id":doc_id}, doc_id=doc_id, book_name_zh = name_zh, book_name_en = name_en)

            print("save [%d] %s" % (ct, doc_id))
            ct += 1

            if name_zh is None and name_en is None:
                print(doc_id, end="\n")
                print(doc)

        cur_batch += 1

    return "ok"


def get_docs(start_page, item_per_page):
    field_config = settings.QIKAN_FIELD_ZH_NAME
    client = MongoClient(settings.QIKAN_DATABASES['HOST'], settings.QIKAN_DATABASES['PORT'])
    db = client.db_qikan
    collection = db.qikan_info
    doc_count = collection.count()  # 总共多少文档
    page_count = doc_count // item_per_page  # 计算出一共多少页
    qikan_docs = collection.find().skip(start_page * item_per_page).limit(item_per_page)
    pre_page = (start_page - 1) if start_page > 1 else 0
    next_page = (start_page + 1) if start_page < page_count else page_count
    cur_page = start_page
    pagger_per_page = settings.PAGGER_COUNT

    return {"qikan_docs": qikan_docs, "field_config": field_config, "doc_count": doc_count,
            "page_count": page_count, "cur_page": cur_page, "pre_page": pre_page, "next_page": next_page,
            "pre_page_link": range(cur_page - pagger_per_page if cur_page > pagger_per_page else 0, cur_page),
            'next_page_link': range(cur_page + 1, cur_page + pagger_per_page)}
