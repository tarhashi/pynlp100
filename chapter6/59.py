import xml.etree.ElementTree as ET
import pydot
import re

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

def split_to_tokens(src):
    return src.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from(tokens):
    token = tokens.pop(0)
    if token == '(':
        first = tokens.pop(0)
        l = []
        while tokens[0] != ')':
            l.append(read_from(tokens))
        tokens.pop(0)
        return (first, l)
    else:
        return token

def parse_string(src):
    return read_from(split_to_tokens(src))

def search_np(src, results = []):
    if not isinstance(src, tuple):
        return
    token = src[0]
    child= src[1]
    if token == 'NP':
        results.append(child)
    for x in child:
        search_np(x, results)

def words_from_result(result):
    ret = []
    for x in result:
        if isinstance(x, tuple):
            ret = ret + words_from_result(x[1])
        else:
            ret = ret + [x]
    return [x.replace('-LRB-', '(').replace('-RRB-', ')') for x in ret]

for sentence in root.iterfind('.//sentences/sentence'):
    parse = sentence.find('./parse').text
    nps = []
    results = []
    search_np(parse_string(parse), results)
    for result in results:
        print(' '.join(words_from_result(result)))