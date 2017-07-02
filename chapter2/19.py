# -*- coding:utf-8 -*-
col1s = [line.split()[0] for line in open('hightemp.txt', 'r').readlines()]
dic = {}
for col1 in col1s:
    dic[col1] = dic.get(col1, 0) + 1

print(sorted(dic.items(), key=lambda x:x[1], reverse=True))