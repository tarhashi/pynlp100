# -*- coding:utf-8 -*-
import redis
import json
import gzip

class RedisDb:
    def __init__(self, host='localhost', port=6379, db=5):
        self.r = redis.Redis(host=host, port=port, db=db)

    def create_db(self, filepath):
        with gzip.open(filepath, 'r') as f:
            for line in f.readlines():
                data = json.loads(line)
                if 'name' in data and 'area' in data:
                    self.r.set(data['name'], data['area'])

    def search_area(self, artist):
        return self.r.get(artist).decode('utf-8')

    def count(self, value):
        return len([1 for key in self.r.keys() if self.r.get(key) == b'Japan'])

    def create_tag_db(self, filepath):
        with gzip.open(filepath, 'r') as f:
            for line in f.readlines():
                data = json.loads(line)
                self.r.set(data['name'], line)

    def find_tag_info(self, name):
        v = self.r.get(name)
        if v:
           data = json.loads(v) 
           return data['tags']
        else:
            return []