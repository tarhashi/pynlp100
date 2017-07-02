# -*- coding:utf-8 -*-
import sys
line_count = int(sys.argv[1])
lines = open('hightemp.txt').readlines()
print("".join(lines[:line_count]))