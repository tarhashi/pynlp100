# -*- coding:utf-8 -*-
from PosiNegaAnalyzer import PosiNegaAnalyzer
import sys

pn = PosiNegaAnalyzer()
pn.set_features('features.txt')
pn.load_model('posinega.pkl.cmp')

coefs = sorted(pn.coefs(), key=lambda x: x[1])
print(coefs[-10:])
print(coefs[:10])