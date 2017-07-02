# -*- coding:utf-8 -*-
from scipy import sparse, io
import pickle

X = io.loadmat('X_300')['X_300']
with open('t.pickle', 'rb') as f:
    t_count = pickle.load(f)
t_index = {}
for i, t in enumerate(t_count.keys()):
    t_index[t] = i
print(X[t_index['United_States']])