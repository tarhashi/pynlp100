import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
sentences = root.findall('.//sentences/sentence')
for sentence in sentences:
    tokens = [token for token in sentence.findall('.//token') if token.find('./POS').text == 'NNP' and token.find('./NER').text == 'PERSON']
    for token in tokens:
        print(token.find('./word').text)
