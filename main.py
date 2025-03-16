from flask import Flask, render_template, request, redirect, url_for, flash, session
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from flask_mail import Mail, Message
import os
from __init__db import User
from db_functions import add_user, is_existing, is_confirmed, set_confirmed, is_password_correct, get_user_by_email
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'noreply@example.com'


mail = Mail(app)

# Инициализация сериализатора для токенов
print(app.config['SECRET_KEY'])
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

@app.errorhandler(404)
def not_found_404(e):
    return render_template("404.html", user = 1)


@app.errorhandler(500)
def not_found_500(e):
    return render_template("500.html", user = 1)

def auth(route):
    def inner(*args, **kwargs):
        if "email" in session:
            return route(*args, **kwargs)
        else:
            return redirect("/sign-in/")
    return inner

@app.route('/')
def index():
    if "email" in session:
        user = 1
    else:
        user = 0
    return render_template('main.html', user = user)

@app.route('/dashboard')
def dashboard():
    user_data = get_user_by_email(session['email'])
    user = {
        "last_name": user_data.last_name,
        "first_name": user_data.first_name,
        "middle_name": user_data.middle_name,
        "email": user_data.email,
        "id": user_data.id,
        "avatar": user_data.avatar
    }
    return render_template('profile.html', user = user)

@app.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if is_existing(email):
            if is_password_correct(email,password):
                session["email"] = email
                return redirect(url_for('index'))
            else:
                flash('Неправильный пароль')
                return redirect(url_for('sign_in'))
        else:
            flash('Неправильный логин или пароль')
            return redirect(url_for('sign_in'))

    return render_template('sign-in.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        if is_existing(email):
             flash('Email уже зарегистрирован')
             return redirect(url_for('sign_up'))
        #Сделать проверку, вдруг пользователь зареган
        add_user(request.form)
        # Генерация токена подтверждения
        token = serializer.dumps(email, salt='email-confirm')

        # Отправка письма
        msg = Message('Подтверждение регистрации на сайте', recipients=[email])
        confirm_url = url_for('confirm_email', token=token, _external=True)
        msg.html = render_template('email_confirmation.html', confirm_url=confirm_url)
        mail.send(msg)
        flash('Письмо с подтверждением отправлено на вашу почту')

    return render_template('sign-up.html', user = 1)

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        # Проверка токена с сроком действия 24 часа
        email = serializer.loads(token, salt='email-confirm', max_age=86400)
    except (SignatureExpired, BadTimeSignature):
        flash('Ссылка подтверждения истекла или неверна')
        return redirect(url_for('sign_in'))

    if is_existing(email):
       if is_confirmed(email):
           flash('Аккаунт уже подтвержден')
       else:
           set_confirmed(email)
           flash('Аккаунт успешно подтвержден!')
    else:
       flash('Пользователь не найден')

    return redirect(url_for('sign_in'))

@app.route("/logout/")
def logout():
    if "email" in session:
        del session["email"]
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)