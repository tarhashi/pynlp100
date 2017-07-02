# -*- coding:utf-8 -*-
w1 = open('col1.txt', 'w')
w2 = open('col2.txt', 'w')
cols = [line.split() for line in open('hightemp.txt', 'r')]
w1.write("\n".join([col[0] for col in cols]))
w2.write("\n".join([col[1] for col in cols]))
w1.close()
w2.close()