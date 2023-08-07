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

    # node info dataset? if node id == node info id:
    # display data on right hand side

    return render_template("maps.html", name = id, nodes = node_data, edges = edge_data)

if __name__ == "__main__":
    app.run("0.0.0.0")

# read from https://github.com/RDFLib/rdflib
