from flask import Flask, render_template
from rdflib import Graph, URIRef, Literal, BNode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", mappings = ['Python', 'Test'])

@app.route("/maps/<id>")
def maps(id):
    graph = Graph()
    graph.parse("schema/Python.ttl", format="turtle")

    node_data = []
    edge_data = []
    node_info = [] # TODO implement this

    current_node = 0
    current_edge = 0

    for s, p, o in graph:

        label_found = False
        for node in node_data:
            if URIRef(s).split('#')[-1] == node['label']:
                label_found = True

        if not label_found:
            node_data.append({ "id": f"{current_node}", "label": f"{URIRef(s).split('#')[-1]}" })
            current_node += 1

    for s, p, o in graph:
        if URIRef(p).split('#')[-1] != "type": # TODO this probably isn't good
            s_id = 0
            o_id = 0

            for node in node_data:
                if node["label"] == URIRef(s).split('#')[-1]:
                    s_id = node["id"]

                if node["label"] == URIRef(o).split('#')[-1]:
                    o_id = node["id"]

            edge_data.append({
                "id": f"{current_edge}",
                "from": f"{s_id}",
                "to": f"{o_id}",
                "label": f"{URIRef(p).split('#')[-1]}",
                "font": { "align": "top" },
                "arrows": "to"
            })

            current_edge += 1

    # node_data = [
    #     {
    #         "id": "1",
    #         "label": "Node 1"
    #     },
    #     {
    #         "id": "2",
    #         "label": "Node 2"
    #     },
    #     {
    #         "id": "3",
    #         "label": "Node 3"
    #     },
    #     {
    #         "id": "4",
    #         "label": "Node 4"
    #     },
    #     {
    #         "id": "5",
    #         "label": "Node 5"
    #     }
    # ]

    # edge_data = [
    #     {
    #         "id": "1",
    #         "from": "1",
    #         "to": "2",
    #         "label": "Test",
    #         "font": { "align": "top" }
    #     },
    #     {
    #         "id": "2",
    #         "from": "1",
    #         "to": "3",
    #         "arrows": "to"
    #     },
    #     {
    #         "id": "3",
    #         "from": "2",
    #         "to": "4"
    #     },
    #     {
    #         "id": "4",
    #         "from": "2",
    #         "to": "5"
    #     }
    # ]

    # node_info = [
    #     {
    #         "id": "1",
    #         "info": "This is some test info!"
    #     }       
    # ]

    return render_template("maps.html", name = id, nodes = node_data, edges = edge_data, info = node_info)

if __name__ == "__main__":
    app.run("0.0.0.0")

# read from https://github.com/RDFLib/rdflib
# https://rdflib.readthedocs.io/en/stable/namespaces_and_bindings.html
# https://stackoverflow.com/questions/28503628/force-rdflib-to-define-a-namespace

# from rdflib.namespace import FOAF, OWL, RDF, RDFS

# g = Graph()
# g.add((URIRef("http://example.org/people/Bob"), RDF.type, Literal("person")))
# print(g.serialize(format="turtle"))
