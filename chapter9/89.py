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
v = X[t_index['Spain']] - X[t_index['Madrid']] + X[t_index['Athens']]
similarities = []
for token in t_index.keys():
    x = X[t_index[token]]
    sim = cosine_similarity(v.reshape(1, -1), x.reshape(1, -1))[0][0]
    similarities.append((token, sim))

for sim in sorted(similarities, key=lambda x: x[1], reverse=True)[:20]:
    print(sim)
