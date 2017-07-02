# -*- coding:utf-8 -*-
import pickle

tc_count = {}
t_count = {}
c_count = {}
N = 0
with open('context.txt', 'r') as f:
    for line in f:
        N = N + 1
        (t, c) = line.strip().split()
        tc_count[(t, c)] = tc_count.get((t, c), 0) + 1
        t_count[t] = t_count.get(t, 0) + 1
        c_count[c] = c_count.get(c, 0) + 1
with open('tc.pickle', 'wb') as f:
    pickle.dump(tc_count, f)
with open('t.pickle', 'wb') as f:
    pickle.dump(t_count, f)
with open('c.pickle', 'wb') as f:
    pickle.dump(c_count, f)
# 68091618
print(N)