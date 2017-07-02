# -*- coding:utf-8 -*-
import pymongo
import gzip
import json

class MongoDb:
    def __init__(self, host='localhost', port=27017, db='testdb'):
        self.mongoclient = pymongo.MongoClient(host=host, port=port)
        self.db = self.mongoclient[db]

    def create_db(self, filepath, collection_name):
        with gzip.open(filepath, 'r') as f:
            for line in f.readlines():
                data = json.loads(line)
                self.db[collection_name].insert_one(data)

    def find_all(self, collection_name, condition):
        return self.db[collection_name].find(condition)

    def count(self, collection_name, condition):
        return self.find_all(collection_name, condition).count()

    def sort(self, collection_name, condition, limit):
        return self.db[collection_name].find().sort(condition, pymongo.DESCENDING).limit(limit)

    def find(self, collection_name, search_condition, sort_key, limit):
        return self.db[collection_name].find(search_condition).sort(sort_key, pymongo.DESCENDING).limit(limit)