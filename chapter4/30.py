# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file

sentences = parse_mecab_file('neko.txt.mecab')
print(sentences[:2])