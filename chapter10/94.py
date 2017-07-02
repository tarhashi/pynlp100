# -*- coding:utf-8 -*-
from gensim.models import word2vec
word2vec_model = word2vec.Word2Vec.load('word2vec.model')

with open('set1.tab', 'r') as r, open('set1_result.txt', 'w') as w:
    for i, line in enumerate(r):
        try:
            if i == 0:
                w.write(line.strip() + "\tsimilarity\n")
            else:
                xs = line.strip().split('\t')
                similarity = word2vec_model.wv.similarity(xs[0], xs[1])
                w.write(line.strip() + '\t{}\n'.format(similarity))
        except KeyError:
            w.write(line.strip() + '\t-1\n')
with open('set2.tab', 'r') as r, open('set2_result.txt', 'w') as w:
    for i, line in enumerate(r):
        try:
            if i == 0:
                w.write(line.strip() + "\tsimilarity\n")
            else:
                xs = line.strip().split('\t')
                similarity = word2vec_model.wv.similarity(xs[0], xs[1])
                w.write(line.strip() + '\t{}\n'.format(similarity))
        except KeyError:
            w.write(line.strip() + '\t-1\n')