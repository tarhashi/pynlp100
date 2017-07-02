# -*- coding:utf-8 -*-
from mongo_db import MongoDb

mongoDb = MongoDb()
for result in mongoDb.find_all('artists', {'name': 'Queen'}):
    print(result)