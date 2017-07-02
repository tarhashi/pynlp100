import xml.etree.ElementTree as ET
import pydot
from itertools import groupby

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

for sentence in root.iterfind('.//sentences/sentence'):
    deps = []
    texts = {}
    for dep in sentence.iterfind('.//dependencies[@type="collapsed-dependencies"]/dep'):
        governor = dep.find('./governor')
        dependent = dep.find('./dependent')
        if dep.attrib['type'] in ['nsubj', 'dobj'] :
            deps.append(
                (
                    dep.attrib['type'] ,
                    governor.attrib['idx'],
                    dependent.attrib['idx']
                )
            )
            texts[governor.attrib['idx']] = governor.text
            texts[dependent.attrib['idx']] = dependent.text

    for key, group in groupby(deps, lambda x: x[1]):
        g = list(group)
        if(len(g) == 2):
            types = [x[0] for x in g]
            if 'nsubj' in types and 'dobj' in types:
                # 並べ替えサボってる
                print('{0}\t{1}\t{2}'.format(
                    texts.get(g[0][2]),
                    texts.get(g[0][1]),
                    texts.get(g[1][2])
                ))