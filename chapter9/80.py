# -*- coding:utf-8 -*-
with open('tokens.txt', 'w') as w:
    with open('enwiki-20150112-400-r100-10576.txt', 'r') as f:
        for line in f.readlines():
            tokens = [x for x in [x.strip('.,!?;:()[]\'"') for x in line.split()] if len(x) > 0]
            if len(tokens) > 0:
                w.write(' '.join(tokens) + '\n')