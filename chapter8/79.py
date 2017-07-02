# -*- coding:utf-8 -*-
from PosiNegaAnalyzer import PosiNegaAnalyzer
import sys
import numpy as np
import matplotlib.pyplot as plt

pn = PosiNegaAnalyzer()
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


i = 0
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
probas = [pn.predict_proba(np.matrix(feature))[0] for feature in  eval_features]

def predict(proba, threshold):
    if proba[0] > threshold:
        return '+1'
    else:
        return '-1'

def calc(labels, probas, threshold):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for act, proba in zip(labels, probas):
        res = predict(proba, threshold)
        if res == '+1' and act == '+1':
            tp += 1
        elif res == '+1' and act == '-1':
            fp += 1
        elif res == '-1' and act == '-1':
            tn += 1
        else:
            fn += 1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    return (precision, recall)

precisions = []
recalls = []
thresholds = []
for threshold in np.arange(0.0, 1.0, 0.01):
    thresholds.append(threshold)
    precision, recall = calc(eval_labels, probas, threshold)
    precisions.append(precision)
    recalls.append(recall)

plt.plot(precisions, recalls)
plt.xlabel('precision')
plt.ylabel('recall')
plt.savefig('precision_recall.png')
plt.clf()
plt.plot(thresholds, precisions)
plt.xlabel('threshold')
plt.ylabel('precision')
plt.savefig('precisions.png')
plt.clf()
plt.plot(thresholds, recalls)
plt.xlabel('threshold')
plt.ylabel('recall')
plt.savefig('recalls.png')
plt.clf()