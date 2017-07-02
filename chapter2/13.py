# -*- coding:utf-8 -*-
col1s = [line[:-1] for line in open('col1.txt', 'r')]
col2s = [line[:-1] for line in open('col2.txt', 'r')]
f = open('merge.txt', 'w')
f.writelines("\n".join(["\t".join(xs) for xs in zip(col1s, col2s)]))