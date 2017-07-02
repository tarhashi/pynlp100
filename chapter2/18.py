# -*- coding:utf-8 -*-
lines = open('hightemp.txt', 'r').readlines()
sorted_lines = sorted(lines, key=lambda x: x.split()[2], reverse=True)
print(sorted_lines)