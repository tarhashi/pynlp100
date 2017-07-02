import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
sentences = root.findall('.//sentences/sentence')
for sentence in sentences:
    tokens = sentence.findall('.//token')
    for token in tokens:
        print('{0}\t{1}\t{2}'.format(token.find('./word').text, token.find('./lemma').text, token.find('./POS').text))