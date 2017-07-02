# -*- coding:utf-8 -*-
f = open('hightemp.txt', 'r')
for line in f:
    print(line.replace("\t", " "), end="")

f.close()