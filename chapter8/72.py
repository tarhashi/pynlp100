# -*- coding:utf-8 -*-

from stop_words import read_stopwords, is_stopword
# from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer
import re

sentiment_file = 'sentiment.txt'
features_file = 'features.txt'
# lemmatizer = WordNetLemmatizer()
stemmer = LancasterStemmer()
stop_words = read_stopwords()

r = re.compile(r'[,.:;\s]')
features = []
with open(sentiment_file, 'r') as f:
    for line in f.readlines():
        words = []
        for word in [word for word in r.split(line)[1:] if len(word) > 1]:
            # lemma = lemmatizer.lemmatize(word)
            # if not is_stopword(lemma, stop_words) and lemma not in features:
            #     features.append(lemma)
            if not is_stopword(word, stop_words):
                stem = stemmer.stem(word)
                if stem not in features:
                    features.append(stem)
with open(features_file, 'w') as f:
    for feature in features:
        f.write(f'{feature}\n')