# -*- coding:utf-8 -*-
from sklearn.linear_model import LogisticRegression
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
from stop_words import read_stopwords, is_stopword
import re

from PosiNegaAnalyzer import PosiNegaAnalyzer

pn = PosiNegaAnalyzer()

pn.set_features('features.txt')
X = []
y = []
with open('sentiment.txt', 'r') as f:
    for line in f.readlines():
        data = line.strip().split(' ', 1)
        y.append(data[0])
        X.append(pn.feature_vectorize(data[1]))
X = np.matrix(X)
pn.fit(X, y)
pn.dump_model('posinega.pkl.cmp')