# -*- coding:utf-8 -*-
from dependency_parse import DependencyParser

sentences = DependencyParser.parse('neko.txt.cabocha')
# sentence = sentences[7]
for sentence in sentences:
    # sentence = sentences[948]
    for chunk in sentence:
        if not chunk.is_include_pos('動詞'):
            continue
    
        idxs = [idx for idx in chunk.srcs if sentence[idx].is_include(pos='名詞', pos1='サ変接続') and sentence[idx].is_include(pos='助詞', base='を')]
        if len(idxs) == 0:
            continue
        verb = ''.join(morph.surface for morph in sentence[idxs[0]].morphs) + chunk.find_pos('動詞')[0].base
        
        particles = ' '.join([sentence[idx].find_pos('助詞')[-1].base for idx in chunk.srcs if sentence[idx].is_include_pos('助詞') and idx not in idxs])
        patterns = ' '.join([''.join([morph.surface for morph in sentence[idx].morphs if morph.pos !='記号']) for idx in chunk.srcs if sentence[idx].is_include_pos('助詞') and idx not in idxs])

        print(f'{verb}\t{particles}\t{patterns}')
