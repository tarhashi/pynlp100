# -*- coding:utf-8 -*-
from gensim.models import word2vec
word2vec_model = word2vec.Word2Vec.load('word2vec.model')

with open('family_result.txt', 'w') as w, open('family.txt', 'r') as f:
    for line in f:
        words = line.strip().split()
        try:
            result = word2vec_model.most_similar(positive=[words[1], words[2]], negative=[words[0]], topn=1)
            w.write(line.strip() + ' {} {}\n'.format(result[0][0], result[0][1]))
        except KeyError:
            w.write(line.strip() + ' None -1\n')
