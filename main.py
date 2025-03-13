from flask import Flask, render_template, request, redirect, url_for, flash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from flask_mail import Mail, Message
import os
from __init__db import User
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@example.com'
app = Flask(__name__)

mail = Mail(app)

# Инициализация сериализатора для токенов
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html", user = 1)


@app.errorhandler(500)
def not_found_500(e):
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

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        # Проверка токена с сроком действия 24 часа
        email = serializer.loads(token, salt='email-confirm', max_age=86400)
    except (SignatureExpired, BadTimeSignature):
        flash('Ссылка подтверждения истекла или неверна')
        return redirect(url_for('sign-up'))

    user = User.query.filter_by(email=email).first()
    if user:
        if user.confirmed:
            flash('Аккаунт уже подтвержден')
        else:
            user.confirmed = True
            flash('Аккаунт успешно подтвержден!')
    else:
        flash('Пользователь не найден')

    return redirect(url_for('sign-in'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)