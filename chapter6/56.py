import xml.etree.ElementTree as ET

def find_rep(sentence_id, token, reps):
    reps = [rep for rep in reps if rep[0].get('sentence')== sentence_id and int(token.attrib['id']) >= rep[0].get('start') and int(token.attrib['id']) <= rep[0].get('end')]
    if (len(reps) > 0):
        return reps[0]
    else:
        return None

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

coreferences = root.iterfind('.//coreference/coreference')

reps = []
for coreference in coreferences:
    representative_mention = None
    mentions = []
    for mention in coreference.iterfind('./mention'):
        dic = {
            'sentence': int(mention.find('./sentence').text),
            'start': int(mention.find('./start').text),
            'end': int(mention.find('./end').text),
            'head': int(mention.find('./head').text),
            'text': mention.find('./text').text
        }
        if 'representative' in mention.attrib and mention.attrib['representative'] == 'true':
            representative_mention = dic
        else:
            print(dic)
            mentions.append(dic)
    for mention in mentions:
        reps.append((mention, representative_mention))

sentences = root.iterfind('.//sentences/sentence')

for sentence in sentences:
    tokens = sentence.findall('.//token')
    for token in tokens:
        rep = find_rep(int(sentence.attrib['id']), token, reps)
        if rep:
            if int(token.attrib['id']) == rep[0].get('start'):
                print('[{0}]'.format(rep[1].get('text')), end=' ')
        else:
            print(token.find('./word').text, end=' ')
    print('')
