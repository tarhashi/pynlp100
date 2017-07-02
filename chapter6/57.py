import xml.etree.ElementTree as ET
import pydot

def find_rep(sentence_id, token, reps):
    reps = [rep for rep in reps if rep[0].get('sentence')== sentence_id and int(token.attrib['id']) >= rep[0].get('start') and int(token.attrib['id']) <= rep[0].get('end')]
    if (len(reps) > 0):
        return reps[0]
    else:
        return None

def write_graph(filename, edges):
    g = pydot.Dot(graph_type='graph')
    for edge in edges:
        node1 = pydot.Node(edge[0][0], label='"{0}"'.format(edge[0][1]))
        node2 = pydot.Node(edge[1][0], label='"{0}"'.format(edge[1][1]))
        g.add_node(node1)
        g.add_node(node2)
        g.add_edge(pydot.Edge(edge[0][0], edge[1][0]))
    g.write_jpeg(filename, prog='dot')

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()

for sentence in root.iterfind('.//sentences/sentence'):
    id = sentence.attrib['id']
    edges = []
    for dependency in sentence.iterfind('.//dependencies[@type="collapsed-dependencies"]'):
        for dep in dependency:
            governor = dep.find('./governor')
            dependent = dep.find('./dependent')
            edges.append(
                (
                    (governor.attrib['idx'], governor.text),
                    (dependent.attrib['idx'], dependent.text)
                )
            )
    if len(edges) > 0:
        write_graph('{0}.jpg'.format(id), edges)