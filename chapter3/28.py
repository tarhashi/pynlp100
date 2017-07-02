# -*- coding:utf-8 -*-

from jawiki import search_by_title, basic_info
import re

text = search_by_title('イギリス')
basic = basic_info(text)
value=''

dic = {}
stress_pattern = re.compile(r"('{2,3}|'{5})\s*([^']+?)\s*\1")
link_pattern = re.compile(r'\[\[([^|\]]+?\|)*(.+?)\]\]')
comment_pattern = re.compile(r'<!--.*?-->')
external_link_pattern = re.compile(r'\[.+?\]')
lang_pattern = re.compile(r'{{lang\|.+?\|(.+?)}}')
for line in basic.split('\n'):
    if line[0] == '|':
        key = line.split('=')[0].strip()[1:]
        val = line.split('=')[1].strip()
        val = stress_pattern.sub(r'\2', val)
        val = link_pattern.sub(r'\2', val)
        val = comment_pattern.sub('', val)
        val = external_link_pattern.sub('', val)
        val = lang_pattern.sub(r'\1', val)
        dic[key] = val
print(dic)