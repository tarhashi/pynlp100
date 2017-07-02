# -*- coding:utf-8 -*-
import random

with open('context.txt', 'w') as w:
    with open('tokens2.txt', 'r') as f:
        for line in f.readlines():
            tokens = line.strip().split()
            for i, token in enumerate(tokens):
                d = random.randint(1, 5)
                for j in range(max(i - d, 0), min(i + d + 1, len(tokens))):
                    if i != j:
                        w.write('{}\t{}\n'.format(token, tokens[j]))