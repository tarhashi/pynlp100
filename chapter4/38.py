# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file, ngram
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

sentences = parse_mecab_file('neko.txt.mecab')
word_counts = {}
for sentence in sentences:
    for morph in sentence:
        word_counts[morph['base']] = word_counts.get(morph['base'], 0) + 1
plt.hist([freq for word, freq in word_counts.items()], bins=100, range=(0, 10000))
plt.xlabel('Term')
plt.ylabel('Freq')
plt.show()