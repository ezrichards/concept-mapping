from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run("0.0.0.0")

# read from https://github.com/RDFLib/rdflib
