# -*- coding:utf-8 -*-
from dependency_parse import DependencyParser

sentences = DependencyParser.parse('neko.txt.cabocha')
for chunk in sentences[7]:
    print(chunk)