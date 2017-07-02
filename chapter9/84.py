# -*- coding:utf-8 -*-
import pickle
from scipy import sparse, io
import math

with open('tc.pickle', 'rb') as f:
    tc_count = pickle.load(f)
with open('t.pickle', 'rb') as f:
    t_count = pickle.load(f)
with open('c.pickle', 'rb') as f:
    c_count = pickle.load(f)
N = 68091618

t_index = {}
c_index = {}
for i, t in enumerate(t_count.keys()):
    t_index[t] = i
for i, c in enumerate(c_count.keys()):
    c_index[c] = i

X = sparse.lil_matrix((len(t_count), len(c_count)))
for k, ftc in tc_count.items():
    t = k[0]
    c = k[1]
    if ftc >= 10:
        X[t_index[t], c_index[c]] = max(math.log(N * ftc / (t_count[t] * c_count[c])), 0)
io.savemat('ppmi_matrix', {'X':X})