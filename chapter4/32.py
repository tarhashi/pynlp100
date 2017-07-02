# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file

sentences = parse_mecab_file('neko.txt.mecab')
verbs = []
for sentence in sentences:
    for m in sentence:
        if m['pos'] == '動詞':
            verbs.append(m)
print(verbs[:10])
