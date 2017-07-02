# -*- coding:utf-8 -*-
from dependency_parse import DependencyParser

sentences = DependencyParser.parse('neko.txt.cabocha')
# sentence = sentences[7]
for sentence in sentences:
    for chunk in sentence:
        if not chunk.is_include_pos('動詞'):
            continue
        if True not in [sentence[idx].is_include_pos('助詞') for idx in chunk.srcs]:
            continue
    
        verb = chunk.find_pos('動詞')[0].base
        particles = ' '.join([sentence[idx].find_pos('助詞')[0].base for idx in chunk.srcs if sentence[idx].is_include_pos('助詞')])
        print(f'{verb}\t{particles}')