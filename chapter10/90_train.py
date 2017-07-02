# -*- coding:utf-8 -*-
from gensim.models import word2vec

sentences = word2vec.LineSentence('tokens2.txt')
model = word2vec.Word2Vec(sentences,size=300, window=10, min_count=10)
model.save('word2vec.model')