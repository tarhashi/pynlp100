# -*- coding:utf-8 -*-

import json
import gzip
import re

def search_by_title(title):
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f.readlines():
            doc = json.loads(line)
            if doc['title'] == title:
                return doc['text']
    return None

def basic_info(text):
    pattern = re.compile(r'{{基礎情報\s.+?\n(|.+?\n)*}}')
    return pattern.search(text).group(0)