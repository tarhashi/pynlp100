# -*- coding:utf-8 -*-

from jawiki import search_by_title, basic_info
import re

text = search_by_title('イギリス')
basic = basic_info(text)
value=''

dic = {}
pattern = re.compile(r"('{2,3}|'{5})\s*([^']+?)\s*\1")
for line in basic.split('\n'):
    if line[0] == '|':
        key = line.split('=')[0].strip()[1:]
        val = line.split('=')[1].strip()
        val = pattern.sub(r'\2', val)
        dic[key] = val
print(dic)