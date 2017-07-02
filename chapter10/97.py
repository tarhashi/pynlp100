# -*- coding:utf-8 -*-
from gensim.models import word2vec
import pickle
import numpy as np
from sklearn.cluster import KMeans

with open('countries_vectors.pickle', 'rb') as f:
    xs = pickle.load(f)
countries = []
with open('countries2.txt', 'r') as f:
    for c in f:
        countries.append(c.strip())
X = np.array(xs)

kmeans = KMeans(n_clusters=5).fit(X)
predicts = kmeans.predict(X)
for (country, cluster) in zip(countries, predicts):
    print(country, cluster)