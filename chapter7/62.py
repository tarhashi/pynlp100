# -*- coding:utf-8 -*-

from redis_db import RedisDb

redis = RedisDb()
print(redis.count('Japan'))
