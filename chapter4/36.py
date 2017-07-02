# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file, ngram

sentences = parse_mecab_file('neko.txt.mecab')
word_counts = {}
for sentence in sentences:
    for morph in sentence:
        word_counts[morph['base']] = word_counts.get(morph['base'], 0) + 1

print(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10])