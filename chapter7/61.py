# -*- coding:utf-8 -*-

from redis_db import RedisDb

redis = RedisDb()
print(redis.search_area('Al Street'))