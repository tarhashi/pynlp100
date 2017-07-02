# -*- coding:utf-8 -*-
import re
from nlp import NLP
from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()
lines = NLP.get_lines('nlp.txt')
line_words = [NLP.get_words(line) for line in lines]

for words in line_words:
    for word in words:
        print('{0}\t{1}'.format(word, st.stem(word)))
    print('')
