# -*- coding:utf-8 -*-

from stop_words import read_stopwords, is_stopword
from nltk.stem.lancaster import LancasterStemmer
import re
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.externals import joblib

class PosiNegaAnalyzer:
    def __init__(self):
        #self.sentiment_file = 'sentiment.txt'
        self.feature_dict = {}
        self.r = re.compile(r'[,.:;\s]')
        self.stemmer = LancasterStemmer()
        self.stop_words = read_stopwords()
        self.lr = LogisticRegression()

    def set_features(self, features_file):
        with open(features_file, 'r') as f:
            for i, line in enumerate(f.readlines()):
                self.feature_dict[line.strip()] = i

    def fit(self, X, y):
        self.lr.fit(X, y)

    def feature_vectorize(self, sentence):
        x = np.zeros(len(self.feature_dict))
        for word in [word for word in self.r.split(sentence) if len(word) > 1]:
            if not is_stopword(word, self.stop_words):
                stem = self.stemmer.stem(word)
                if stem in  self.feature_dict:
                    x[self.feature_dict[stem]] = 1
        return x

    def predict(self, X):
        return self.lr.predict(X)

    def predict_proba(self, X):
        return self.lr.predict_proba(X)

    def dump_model(self, filename):
        joblib.dump(self.lr, filename, compress=True)

    def load_model(self, filename):
        self.lr = joblib.load(filename)

    def coefs(self):
        return [
            x for x in zip(
                [x[0] for x in sorted(self.feature_dict.items(), key=lambda x: x[1])],
                self.lr.coef_[0]
            )]

    def split_training_sets(self, labels, features):
        len = len()
