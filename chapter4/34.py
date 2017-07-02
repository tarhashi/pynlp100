# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file, ngram

sentences = parse_mecab_file('neko.txt.mecab')
a_no_bs = []
for sentence in sentences:
    if len(sentence) > 2:
        trigrams = ngram(sentence, 3)
        for trigram in trigrams:
            if trigram[0]['pos'] == '名詞' and trigram[2]['pos'] == '名詞' and trigram[1]['surface'] == 'の' and trigram[1]['pos1'] == '連体化':
                a_no_bs.append(trigram)
print(a_no_bs[:3])
