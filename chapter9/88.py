# -*- coding:utf-8 -*-
from scipy import sparse, io
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

X = io.loadmat('X_300')['X_300']
with open('t.pickle', 'rb') as f:
    t_count = pickle.load(f)
t_index = {}
for i, t in enumerate(t_count.keys()):
    t_index[t] = i
engrand = X[t_index['England']]
similarities = []
for token in t_index.keys():
    if token == 'England':
        continue
    x = X[t_index[token]]
    sim = cosine_similarity(engrand.reshape(1, -1), x.reshape(1, -1))[0][0]
    similarities.append((token, sim))

for sim in sorted(similarities, key=lambda x: x[1], reverse=True)[:10]:
    print(sim)