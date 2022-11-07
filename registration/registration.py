from flask import Blueprint, render_template, url_for, request, flash, session, redirect, abort
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, app
from models import Client


reg = Blueprint('registration', __name__, template_folder='templates')


@app.route('/')
@reg.route('/', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile', day_number='0'))

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
                db.session.commit()
                login_user(new_client, remember=True)
                return redirect(url_for('.login'))
        except:
            db.session.rollback()
    #
    return render_template('registration/register.html', title='Регистрация')


@reg.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('profile', day_number='0'))

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('psw')

    if name and password and email:
        client = Client.query.filter_by(email=email).first()

        if client and check_password_hash(client.psw, password):

            if check_password_hash(client.psw, password) is False:
                flash('Пароль заполнен не верно', category='error')

            remember = True if request.form.get('remember_me') else False
            login_user(client, remember=remember)
            next_page = request.args.get('next')

            if next_page is not None:
                return redirect(url_for(next_page))
            else:
                return redirect(url_for('day_marathon', day_number='0'))
        else:
            flash(f'Пользователя с email "{email}" нет в базе', category='error')
    else:
        flash('Пожалуйста, заполните все поля', category='alert')

    return render_template('registration/login.html', title='Авторизация')


@reg.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))