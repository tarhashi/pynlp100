# -*- coding:utf-8 -*-
from dependency_parse import Morph

with open('neko.txt.cabocha', 'r') as f:
    sentenses = []
    morphs = []
    for line in f.readlines():
        if line.strip() == 'EOS':
            if len(morphs) > 0:
                sentenses.append(morphs)
                morphs = []
        elif line[0] != '*':
            surface, x = line.split('\t', 1)
            data = x.split(',')
            morphs.append(Morph(surface, data[6], data[0], data[1]))
    for morph in sentenses[2]:
        print(morph)