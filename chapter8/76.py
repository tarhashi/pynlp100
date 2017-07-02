# -*- coding:utf-8 -*-
from PosiNegaAnalyzer import PosiNegaAnalyzer
import sys
import numpy as np

pn = PosiNegaAnalyzer()
pn.set_features('features.txt')
pn.load_model('posinega.pkl.cmp')

with open('result.txt', 'w') as w:
    with open('sentiment.txt', 'r') as f:
        for line in f.readlines():
            (label, text) = line.strip().split(None, 1)
            X = np.matrix(pn.feature_vectorize(text))
            w.writelines('{0}\t{1}\t{2}\n'.format(
                label, pn.predict(X)[0], max(pn.predict_proba(X)[0])
            ))