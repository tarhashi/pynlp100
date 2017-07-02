# -*- coding:utf-8 -*-

from jawiki import search_by_title
import re

pattern = re.compile(r"\[\[Category:(.+?)\]\]")
text = search_by_title('イギリス')
categories = [category.split('|')[0] for category in pattern.findall(text)]
print(categories)