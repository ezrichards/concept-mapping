from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/network/<id>")
def network(id):
    return render_template("network.html", name = id)

if __name__ == "__main__":
    app.run("0.0.0.0")

# read from https://github.com/RDFLib/rdflib
