# -*- coding:utf-8 -*-

from jawiki import search_by_title, basic_info
import re
import requests

text = search_by_title('イギリス')
basic = basic_info(text)
value=''

dic = {}
for line in basic.split('\n'):
    if line[0] == '|':
        key = line.split('=')[0].strip()[1:]
        val = line.split('=')[1].strip()
        dic[key] = val

url = 'https://en.wikipedia.org/w/api.php'
img = dic['国旗画像']
params = {'action': 'query', 'prop': 'imageinfo', 'format': 'json', 'iiprop': 'url', 'titles': f'Image:{img}'}
res = requests.get(url, params=params).json()
print(res['query']['pages']['23473560']['imageinfo'][0]['url'])