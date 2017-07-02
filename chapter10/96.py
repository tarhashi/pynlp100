# -*- coding:utf-8 -*-
from gensim.models import word2vec
import pickle

word2vec_model = word2vec.Word2Vec.load('word2vec.model')
with open('countries.txt', 'r') as f, open('countries_vectors.pickle', 'wb') as w, open('countries2.txt', 'w') as w2:
    vectors = []
    for line in f:
        try:
            c = line.strip().replace(' ', '_')
            vectors.append(word2vec_model.wv[c])
            w2.write(c + '\n')
        except:
            continue
    pickle.dump(vectors, w)