# -*- coding:utf-8 -*-
from dependency_parse import DependencyParser
import pydot

sentences = DependencyParser.parse('neko.txt.cabocha')
sentence = sentences[7]
edges = []
for chunk in sentence:
    dst_surface = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
    for idx in chunk.srcs:
        src_chunk = sentence[idx]
        src_surface = ''.join([morph.surface for morph in src_chunk.morphs if morph.pos != '記号'])
        edges.append((dst_surface, src_surface))

g = pydot.graph_from_edges(edges)
g.write_jpeg('44.jpg', prog='dot')