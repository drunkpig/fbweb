# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId


def index(request):

    client = MongoClient(settings.QIKAN_DATABASES['HOST'], settings.QIKAN_DATABASES['PORT'])
    db = client.db_qikan
    collection = db.qikan_info
    data = collection.find_one({"_id":ObjectId("55f4372fc777807d9fd74934")})
    return render(request, "web/index.html", {"qikan":data})