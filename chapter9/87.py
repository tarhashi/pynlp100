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
united_states = X[t_index['United_States']]
us = X[t_index['U.S']]

print(cosine_similarity(united_states.reshape(1, -1), us.reshape(1, -1)))