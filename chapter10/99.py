# -*- coding:utf-8 -*-
import pickle
import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

with open('countries_vectors.pickle', 'rb') as f:
    xs = pickle.load(f)
countries = []
with open('countries2.txt', 'r') as f:
    for c in f:
        countries.append(c.strip())
X = np.array(xs)
tsne = TSNE(n_components=2)
result = tsne.fit_transform(X)
print(result)
plt.plot(result[:, 0], result[:, 1], '.')
plt.show()