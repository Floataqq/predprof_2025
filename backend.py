from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
@app.route("/3d")
def threed():
    return render_template("3d.html")


@app.route("/data")
def give_tiles():
    with open("dump.txt", 'r') as f:
        return [json.loads(i) for i in f.readlines()]
        
