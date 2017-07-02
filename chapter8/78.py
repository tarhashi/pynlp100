from PosiNegaAnalyzer import PosiNegaAnalyzer
import numpy as np
# -*- coding:utf-8 -*-
from sklearn.metrics import classification_report

pn = PosiNegaAnalyzer()
pn.set_features('features.txt')
labels = []
features = []
with open('sentiment.txt') as f:
    for line in f.readlines():
        (label, txt) = line.strip().split(None, 1)
        labels.append(label)
        features.append(pn.feature_vectorize(txt))

splitted_labels = ([], [], [], [], [])
splitted_features = ([], [], [], [], [])

for i in range(len(labels)):
    idx = i % 5
    splitted_labels[idx].append(labels[i])
    splitted_features[idx].append(features[i])


for i in range(len(splitted_labels)):
    train_features = []
    train_labels = []
    eval_features = None
    eval_labels = None
    for j in range(len(splitted_labels)):
        if i == j:
            eval_features = splitted_features[j]
            eval_labels = splitted_labels[j]
        else:
            train_features.extend(splitted_features[j])
            train_labels.extend(splitted_labels[j])
    train_features = np.matrix(train_features)
    pn.fit(train_features, train_labels)
    predicts = pn.predict(eval_features)
    print(classification_report(eval_labels, predicts))
