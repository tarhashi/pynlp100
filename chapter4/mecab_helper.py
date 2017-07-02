# -*- coding:utf-8 -*-
import MeCab

def line_to_dic(line):
    surface, x = line.split('\t', 2)
    data = x.split(',')
    return {'surface': surface, 'base': data[6], 'pos': data[0], 'pos1': data[1]}

def parse_mecab_file(path):
    sentences = []
    morphemes = []
    for line in open(path).readlines():
        if line == 'EOS\n':
            if len(morphemes) > 0:
                sentences.append(morphemes)
                morphemes = []
        else:
            morphemes.append(line_to_dic(line))
    return sentences

def ngram(seq, n):
    return [seq[i:i+n] for i in range(0, len(seq) - n + 1)]