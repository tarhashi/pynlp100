# -*- coding:utf-8 -*-
from mongo_db import MongoDb

mongoDb = MongoDb()
for result in mongoDb.sort('artists', "rating.count", 10):
    print(result)
