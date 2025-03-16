from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
@app.route("/3d")
def threed():
    return render_template("3d.html")


def visualise(api_url):
        
