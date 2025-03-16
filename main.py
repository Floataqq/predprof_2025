from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from __init__db import User
from db_functions import add_user, is_existing, is_confirmed, set_confirmed, is_password_correct


app = Flask()

@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html", user = 1)


@app.errorhandler(500)
def not_found_500(e):
    return render_template("500.html", user = 1)

@app.route('/')
def index():
    return render_template('main.html', user = user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)