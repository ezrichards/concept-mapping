from rdflib import Graph
g = Graph()
g.parse('https://www.w3.org/2000/01/rdf-schema#')

for s, p, o in g:
    print(s, p, o)
