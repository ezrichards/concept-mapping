from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", mappings = ['Python', 'Test'])

@app.route("/maps/<id>")
def maps(id):
    node_data = [
        {
            "id": "1",
            "label": "Node 1"
        },
        {
            "id": "2",
            "label": "Node 2"
        },
        {
            "id": "3",
            "label": "Node 3"
        },
        {
            "id": "4",
            "label": "Node 4"
        },
        {
            "id": "5",
            "label": "Node 5"
        }
    ]

    edge_data = [
        {
            "id": "1",
            "from": "1",
            "to": "2",
            "label": "Test",
            "font": { "align": "top" }
        },
        {
            "id": "2",
            "from": "1",
            "to": "3",
            "arrows": "to"
        },
        {
            "id": "3",
            "from": "2",
            "to": "4"
        },
        {
            "id": "4",
            "from": "2",
            "to": "5"
        }
    ]

    node_info = [
        {
            "id": "1",
            "info": "This is some test info!"
        }       
    ]

    return render_template("maps.html", name = id, nodes = node_data, edges = edge_data, info = node_info)

if __name__ == "__main__":
    app.run("0.0.0.0")

# read from https://github.com/RDFLib/rdflib
# https://rdflib.readthedocs.io/en/stable/namespaces_and_bindings.html
# https://stackoverflow.com/questions/28503628/force-rdflib-to-define-a-namespace

# from rdflib import Graph, URIRef, Literal, BNode
# from rdflib.namespace import FOAF, OWL, RDF, RDFS

# g = Graph()
# g.parse('https://www.w3.org/2000/01/rdf-schema#')
# for s, p, o in g:
#     print(s, p, o)

# g = Graph()
# g.add((URIRef("http://example.org/people/Bob"), RDF.type, Literal("person")))
# print(g.serialize(format="turtle"))
