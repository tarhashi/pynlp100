# -*- coding:utf-8 -*-
from gensim.models import word2vec

model = word2vec.Word2Vec.load('word2vec.model')
print('Vector')
print(model.wv['United_States'])
print('Similarity')
print(model.wv.similarity('United_States', 'U.S'))
print('Most Similar')
results = model.most_similar(positive='England', topn=10)
print(results)
print('Spain - Madrid + Athens')
results2 = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
print(results2)