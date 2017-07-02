# -*- coding:utf-8 -*-
from mongo_db import MongoDb

mongoDb = MongoDb()
print(mongoDb.count('artists', {'area': 'Japan'}))