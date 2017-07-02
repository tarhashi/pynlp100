# -*- coding:utf-8 -*-
from PosiNegaAnalyzer import PosiNegaAnalyzer
import sys
import numpy as np

pn = PosiNegaAnalyzer()
pn.set_features('features.txt')
pn.load_model('posinega.pkl.cmp')

text = sys.argv[1]
feature_vec = np.matrix(pn.feature_vectorize(text))
print(pn.predict(feature_vec)[0])
print(max(pn.predict_proba(feature_vec)[0]))
