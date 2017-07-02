import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
sentences = root.findall('.//sentences/sentence')
for sentence in sentences:
    tokens = sentence.findall('.//token')
    for token in tokens:
        print(token.find('./word').text)
    print('')