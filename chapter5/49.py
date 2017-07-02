# -*- coding:utf-8 -*-
from dependency_parse import DependencyParser

def get_path(sentence, path, chunk):
    path.append(chunk)
    if chunk.dst == -1:
        return path
    else:
        return get_path(sentence, path, sentence[chunk.dst])

def search_path(chunk, paths):
    for path in paths:
        for c in path:
            if chunk == c:
                return path

def search_partial_path(pair, path):
    ret = []
    found_x = False
    for chunk in path:
        if found_x:
            ret.append(chunk)
            if chunk == pair[1]:
                return ret
        else:
            if chunk == pair[0]:
                found_x = True
                ret.append(chunk)
    return None
def make_paths(path1, path2):
    set1 = set(path1)
    set2 = set(path2)
    product_set = set1 & set2
    return (sorted(set1 - product_set, key=path1.index), sorted(set2 - product_set, key=path2.index), sorted(product_set, key=path1.index))

def make_string(path, x=None, y=None):
    ret = []
    for chunk in path:
        if chunk == x:
            noun = chunk.find_pos('名詞')[0]
            ret.append(chunk.surface().replace(noun.surface, 'X'))
        elif chunk == y:
            noun = chunk.find_pos('名詞')[0]
            ret.append(chunk.surface().replace(noun.surface, 'Y'))
        else:
            ret.append(chunk.surface())
    return ' -> '.join(ret)

sentences = DependencyParser.parse('neko.txt.cabocha')
i = 0
for sentence in sentences:
    paths = []
    sentence = sentences[7]
    if i > 0:
        break
    i = i + 1
    if len([chunk for chunk in sentence if chunk.is_include(pos='名詞')]) < 2:
        continue
    for chunk in sentence:
        if not chunk.is_include(pos='名詞'):
            continue
        if chunk.dst == -1:
            continue
        path = get_path(sentence, [], chunk)
        paths.append(path)
    pairs = []
    for i in range(len(sentence)):
        if sentence[i].is_include(pos='名詞'):
            for j in range(i+1, len(sentence)):
                if sentence[j].is_include(pos='名詞'):
                    pairs.append((sentence[i], sentence[j]))
    for pair in pairs:
        print(pair[0].surface(), pair[1].surface())
        x_path = search_path(pair[0], paths)
        partial_path = search_partial_path(pair, x_path)
        if partial_path is not None:
            print(make_string(partial_path, x=pair[0], y=pair[1]))
        else:
            y_path = search_path(pair[1], paths)
            ps = make_paths(x_path, y_path)
            print(make_string(ps[0], x=pair[0]), end='')
            print(' | ', end='')
            print(make_string(ps[1], y=pair[1]), end='')
            print(' | ', end='')
            print(make_string(ps[2]))