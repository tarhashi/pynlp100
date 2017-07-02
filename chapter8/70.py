# -*- coding:utf-8 -*-
import random

pos_file = 'rt-polaritydata/rt-polarity.pos'
neg_file = 'rt-polaritydata/rt-polarity.neg'
out_file = 'sentiment.txt'
encoding = 'latin_1'

pos_lines = ['+1 {}'.format(line.strip()).encode('utf-8').decode('utf-8') for line in open(pos_file, 'r', encoding=encoding).readlines()]
neg_lines = ['-1 {}'.format(line.strip()).encode('utf-8').decode('utf-8') for line in open(neg_file, 'r', encoding=encoding).readlines()]
pos_count = len(pos_lines)
neg_count = len(neg_lines)
lines = pos_lines + neg_lines
random.shuffle(lines)
with open(out_file, 'w') as f:
    f.write('\n'.join(lines))

print('positive: {}, negative: {}'.format(pos_count, neg_count))