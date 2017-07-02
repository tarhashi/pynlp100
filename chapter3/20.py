# -*- coding:utf-8 -*-
import json
import gzip

docs = {}
with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f.readlines():
       doc = json.loads(line)
       docs[doc['title']] = doc['text']

print(docs['イギリス'])