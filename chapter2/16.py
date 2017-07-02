# -*- coding:utf-8 -*-
import sys
count = int(sys.argv[1])
lines = open('hightemp.txt').readlines()
elm_count = len(lines) // count

def divide(seq, elm_count):
    if len(seq) > elm_count:
        return [seq[:elm_count]] + divide(seq[elm_count:], elm_count)
    else:
        return [seq]

print(divide(lines, elm_count))