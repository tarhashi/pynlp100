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
xs = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
ranks = np.arange(len(xs)) + 1
freqs = [freq for word, freq in xs]
plt.scatter(ranks, freqs)
plt.xlabel('Term Freq')
plt.ylabel('Freq')
plt.xscale('log')
plt.yscale('log')
plt.show()
# plt.hist([freq for word, freq in word_counts.items()], bins=100, range=(0, 10000))
# plt.xlabel('Term Frequency')
# plt.ylabel('Freqency')
# plt.show()