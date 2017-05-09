import os, sys
from pymongo import MongoClient
from django.conf import settings
from bson.objectid import ObjectId
from math import ceil

script_path = sys.path[0]
proj_path = script_path + "/../"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fbweb.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
from web.models import Qikan

"""
把mongodb里的settings.SYNC_FIELDS同步到default db
:param request:
:return:
"""
client = MongoClient('dev.mongo.jscrapy.org', 27017)
db_name = sys.argv[1]
collection_name = sys.argv[2]
db = client[db_name]
collection = db[collection_name]

ct = 0;
# 插入default RDBM
qikan_docs = collection.find()
for doc in qikan_docs:
    doc_id = str(doc['_id'])
    qk = Qikan()
    for k, v in doc.items():
        setattr(qk, k, v)
    try:
        qk.save()
    except Exception as ex:
        print(ex)

    print("save [%d] %s" % (ct, doc_id))
    ct += 1
