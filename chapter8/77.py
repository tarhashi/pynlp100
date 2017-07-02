# -*- coding:utf-8 -*-
from sklearn.metrics import classification_report
labels = []
predicts = []
with open('result.txt', 'r') as f:
    for line in f.readlines():
        (label, predict, score) = line.strip().split()
        labels.append(label)
        predicts.append(predict)
print(classification_report(labels, predicts))