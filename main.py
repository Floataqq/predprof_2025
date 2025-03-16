import json
import api
from flask import Flask, render_template, request, redirect, url_for, flash, session
#
# from db_functions import add_user, is_existing, is_confirmed, set_confirmed, is_password_correct
# from backend import visualise

app = Flask(__name__)
api_url = "https://olimp.miet.ru/ppo_it/api"


@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html", user = 1)


@app.errorhandler(500)
def not_found_500(e):
    return render_template("500.html", user = 1)

@app.route('/', methods=["GET", "POST"])
@app.route('/3d', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        api_url = request.form["api_url"]
        visualise(api_url)
    return render_template("3d.html")

@app.route("/coords")
def coords():
    api_url = request.args.get("api_url") or \
        "https://olimp.miet.ru/ppo_it/api"
    return api.get_coords(api_url)

@app.route("/data")
def give_tiles():
    with open("dump.txt", 'r') as f:
        return [json.loads(i) for i in f.readlines()]

@app.route("/stations")
def stations():
    #как-то берем вершины
    data = []
    response = []
    for i in data:
        d1 = dict()
        d1["cords"] = data[0]
        d1["type"] = data[1]
        response.append(d1)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
