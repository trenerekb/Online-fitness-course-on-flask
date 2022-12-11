import random

from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, app
from config import Configuration
from models import Client, Profile

reg = Blueprint('registration', __name__, template_folder='templates')


@app.route('/')
@reg.route('/', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profiles.profile_view'))

    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    password1 = request.form.get('psw1')
    password2 = request.form.get('psw2')

    if request.method == 'POST':
        try:
            client = Client.query.filter_by(email=email).first()
            if client:
                flash('Пользователь с таким email уже существует', category='error')
            elif not(name or surname or password1 or password2):
                flash('Пожалуйста, заполните все поля', category='error')
            elif password1 != password2:
                flash('Неверный повторный пароль', category='error')
            else:
                hash_psw = generate_password_hash(password1)
                new_client = Client(name=name, surname=surname, email=email, psw=hash_psw)
                db.session.add(new_client)
                db.session.flush()

                new_profile = Profile(client_id=new_client.id, avatar_client=random.choice(Configuration.avatar_default))
                db.session.add(new_profile)
                db.session.commit()
                login_user(new_client, remember=True)
                return redirect(url_for('.login'))
        except:
            flash('Регистрация не удалась. Попробуйте еще раз', category='error')
            db.session.rollback()
            return redirect(url_for('registration.register'))

    return render_template('registration/register.html', title='Регистрация')


@reg.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profiles.profile_view'))

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('psw')

    if name and password and email:
        client = Client.query.filter_by(email=email).first()

        if client:

            if check_password_hash(client.psw, password) is False and client.psw != password:
                flash('Пароль заполнен не верно', category='error')
                return redirect(url_for('.login'))

            remember = True if request.form.get('remember_me') else False
            login_user(client, remember=remember)
            next_page = request.args.get('next')

            if next_page is not None:
                return redirect(url_for(next_page))
            else:
                return redirect(url_for('days.day_marathon', day_number='0'))
        else:
            flash(f'Пользователя с email "{email}" нет в базе', category='error')
            return redirect(url_for('.login'))
    else:
        flash('Пожалуйста, заполните все поля', category='alert')
        return render_template('registration/login.html', title='Авторизация')


@reg.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))