# -*- coding:utf-8 -*-
from dependency_parse import DependencyParser

def get_path(sentence, path, chunk):
    path.append(chunk)
    if chunk.dst == -1:
        return path
    else:
        return get_path(sentence, path, sentence[chunk.dst])

sentences = DependencyParser.parse('neko.txt.cabocha')
# sentence = sentences[7]
paths = []
for sentence in sentences:
    for chunk in sentence:
        if not chunk.is_include(pos='名詞'):
            continue
        if chunk.dst == -1:
            continue
        path = get_path(sentence, [], chunk)
        paths.append(path)
for path in paths:
    str = ' -> '.join([chunk.surface() for chunk in path])
    print(str)
