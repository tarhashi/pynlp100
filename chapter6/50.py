# -*- coding:utf-8 -*-
import re

lines = []
with open('nlp.txt', 'r') as f:
    split_pattern = re.compile(r'[?.;:!]\s+?(?=[A-Z])')
    end_pattern = re.compile(r'[?.;:!]?\s+?$')
    for line in f.readlines():
        if line == '\n':
            continue
        lines = lines + [re.sub(end_pattern, '', line) for line in split_pattern.split(line)]
for line in lines:
    print(line)