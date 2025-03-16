import json
import api
from flask import Flask, render_template, request, redirect, url_for, flash, session
#
# from db_functions import add_user, is_existing, is_confirmed, set_confirmed, is_password_correct
# from backend import visualise, get_stations, do_map
from backend import get_stations

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
        order = [0, 15, 4, 7, 11, 1, 6, 9, 5, 13, 3, 2, 12, 10, 14, 8]
        data = [json.loads(i) for i in f.readlines()]
        return [data[i] for i in order]

@app.route("/stations")
def stations():
    api_url = request.args.get("api_url") or \
              "https://olimp.miet.ru/ppo_it/api"
    data = get_stations(api_url)
    response = []
    for i in data:
        d1 = dict()
        d1["cords"] = i[0]
        d1["type"] = i[1]
        response.append(d1)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
