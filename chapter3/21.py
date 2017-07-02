# -*- coding:utf-8 -*-

from jawiki import search_by_title
import re

pattern = re.compile(r"\[\[Category:.+?\]\]")
text = search_by_title('イギリス')
matched_lines = pattern.findall(text)
print(matched_lines)