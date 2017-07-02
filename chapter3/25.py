# -*- coding:utf-8 -*-

from jawiki import search_by_title, basic_info
import re

text = search_by_title('イギリス')
basic = basic_info(text)
value=''

dic = {}
for line in basic.split('\n'):
    if line[0] == '|':
        key = line.split('=')[0].strip()[1:]
        val = line.split('=')[1].strip()
        dic[key] = val
print(dic)