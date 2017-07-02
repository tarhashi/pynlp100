# -*- coding:utf-8 -*-

from jawiki import search_by_title
import re

pattern = re.compile(r"(={2,})\s*(.+?)\s*={2,}")
text = search_by_title('イギリス')
matches = pattern.findall(text)
sections = [ (match[1], len(match[0]) - 1) for match in matches ]
print(sections)