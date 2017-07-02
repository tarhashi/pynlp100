# -*- coding:utf-8 -*-

from redis_db import RedisDb

redis = RedisDb()

redis.create_db('artist.json.gz')