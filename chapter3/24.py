# -*- coding:utf-8 -*-

from jawiki import search_by_title
import re

pattern = re.compile(r"(?:File|ファイル):(.+?)\|")
text = search_by_title('イギリス')
matches = pattern.findall(text)
print(matches)