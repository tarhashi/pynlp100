# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file, ngram
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'AppleGothic'

sentences = parse_mecab_file('neko.txt.mecab')
word_counts = {}
for sentence in sentences:
    for morph in sentence:
        word_counts[morph['base']] = word_counts.get(morph['base'], 0) + 1
top10 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
label = [x[0] for x in top10]
left = np.arange(10)
height = [x[1] for x in top10]
plt.bar(left, height, tick_label=label)
plt.xlabel('Term')
plt.ylabel('Freq')
plt.show()