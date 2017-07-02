# -*- coding:utf-8 -*-
import pickle
import numpy as np
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

with open('countries_vectors.pickle', 'rb') as f:
    xs = pickle.load(f)
countries = []
with open('countries2.txt', 'r') as f:
    for c in f:
        countries.append(c.strip())
X = np.array(xs)
cluster = ward(X)
print(cluster)
dendrogram(cluster, labels=countries)
plt.show()