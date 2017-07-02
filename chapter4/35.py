# -*- coding:utf-8 -*-
from mecab_helper import parse_mecab_file, ngram

sentences = parse_mecab_file('neko.txt.mecab')
connections = []
for sentence in sentences:
    if len(sentence) > 1:
        connection = []
        for m in sentence:
            if m['pos'] == '名詞':
                connection.append(m)
            else:
                if len(connection) > 1:
                    connections.append(connection)
                connection = []
print(connections[:5])
