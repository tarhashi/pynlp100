# -*- coding:utf-8 -*-

from redis_db import RedisDb

redis = RedisDb(db=6)

print(redis.find_tag_info('WIK▲N'))
#redis.create_tag_db('artist.json.gz')
