from flask import Flask, render_template, session, request, redirect, url_for, flash

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", user = 1)


@app.errorhandler(500)
def not_found(e):
    return render_template("500.html", user = 1)

@app.route('/')
def index():
    return render_template('main.html', user = 1)

@app.route('/dashboard')
def dashboard():
    user = {
        "last_name": "Иванов",
        "first_name": "Иван",
        "middle_name": "Иванович",
        "email": "ivanov@mail.ru",
        "id": "1",
        "avatar": None
    }
    return render_template('profile.html', user = user)

@app.route('/sign-in')
def sign_in():
    return render_template('sign-in.html', user = 1)

@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html', user = 1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)