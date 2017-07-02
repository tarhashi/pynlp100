# -*- coding:utf-8 -*-
import numpy
with open('set1_result.txt', 'r') as f1, open('set2_result.txt', 'r') as f2:
    rank = []
    a1 = []
    a2 = []
    for i, line in enumerate(f1):
        if i > 0:
            xs = line.strip().split('\t')
            a1.append(float(xs[2]))
            a2.append(float(xs[-1]))
            rank.append((xs[0], xs[1], xs[-1]))
    for i, line in enumerate(f2):
        if i > 0:
            xs = line.strip().split('\t')
            a1.append(float(xs[2]))
            a2.append(float(xs[-1]))
            rank.append((xs[0], xs[1], xs[-1]))

rank = sorted(rank, key=lambda x: x[2], reverse=True)
print(rank[0:10])
N = len(a1)
print(1 - (6 * sum(numpy.array(a1) - numpy.array(a2)) ** 2) / (N**3 - N))
