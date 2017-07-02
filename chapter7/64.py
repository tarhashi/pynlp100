# -*- coding:utf-8 -*-
from mongo_db import MongoDb

mongoDb = MongoDb()
mongoDb.create_db('artist.json.gz', 'artists')