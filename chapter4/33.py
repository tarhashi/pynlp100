# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file

sentences = parse_mecab_file('neko.txt.mecab')
sahens = []
for sentence in sentences:
    for m in sentence:
        if m['pos'] == '名詞' and m['pos1'] == 'サ変接続':
            sahens.append(m)
print(sahens[:10])