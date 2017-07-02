# -*- coding:utf-8 -*-
from dependency_parse import DependencyParser

sentences = DependencyParser.parse('neko.txt.cabocha')
sentence = sentences[7]
for chunk in sentence:
    if not chunk.is_include_pos('動詞'):
        continue
    if True not in [sentence[idx].is_include_pos('名詞') for idx in chunk.srcs]:
        continue

    dst_surface = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
    src_surfaces = []
    for idx in chunk.srcs:
        src_chunk = sentence[idx]
        src_surface = ''.join([morph.surface for morph in src_chunk.morphs if morph.pos != '記号'])
        src_surfaces.append(src_surface)
    print('\t'.join([dst_surface] + src_surfaces))
