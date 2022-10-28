import os

from flask import render_template, url_for, request, flash, session, redirect, abort
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from app import app, db
from config import Configuration
from models import Client


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Configuration.ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

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
                return redirect(url_for('login'))
        except:
            db.session.rollback()

    return render_template('register.html', title='Регистрация')


@app.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('psw')

    if name and password and email:
        client = Client.query.filter_by(email=email).first()
        print(client.psw)
        if client and check_password_hash(client.psw, password):
            print(check_password_hash(client.psw, password))
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

    return render_template('login.html', title='Авторизация')


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login'))

    return response


@app.route('/profile')
@login_required
def profile():
    # if 'userLogged' not in session or session['userLogged'] != username:
    #     abort(401)
    return render_template('profile.html', title='Профиль', username=current_user)


@app.route('/day/<day_number>')
@login_required
def day_marathon(day_number):

    count_days_list = [x for x in range(22)]
    text_report_current_user = 'Hello, I am Ruslan'
    date_report_current_user = '25-09-2022'
    user_name_comment = 'Vasay'
    user_name_reply = 'Anna G'
    date_comment = '11-09-2022'
    comment = 'kfjns dkgfbd sfghlbsd glbgl hsbdgl'
    reply_comment = 'bdabgf asdhbas'
    date_reply_comment = '15-09-2022'
    video = 'video/vid-1.mp4'
    video_title = "Видео знакомство"
    task_description = 'описание задания'

    if day_number == '0':
        print(current_user.role)
        return render_template('day0.html', count_days=count_days_list, title=f'День {day_number}', video=video,
                               video_title=video_title, header=f'День {day_number}',
                               task_description=task_description, user_name_comment=user_name_comment, date_comment=date_comment, comment=comment,
                               user_name_reply=user_name_reply, date_reply_comment=date_reply_comment,
                               reply_comment=reply_comment, text_report_current_user=text_report_current_user,
                               date_report_current_user=date_report_current_user)
    else:
        return render_template('day.html', count_days=count_days_list, title=f'День {day_number}', video=video,
                               video_title = video_title, header=f'День {day_number}',
                               task_description=task_description, current_user=current_user.name,
                               user_name_comment=user_name_comment, date_comment=date_comment, comment=comment,
                               user_name_reply=user_name_reply, date_reply_comment=date_reply_comment,
                               reply_comment=reply_comment, text_report_current_user=text_report_current_user,
                               date_report_current_user=date_report_current_user)


@app.route('/user_comment')
def get_user_comment():
    pass
    # comment = User.get_сomment()


@app.route('/add_report', methods=['POST', 'GET'])
def add_report():
    if request.method == 'POST':
        text = request.form['text_report']
        files = request.files.getlist('file')

        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('day.html')

        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        #
        # file = request.files['file']
        # file.save(app.config["UPLOAD_FOLDER"])
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     text = request.form['text_report']
        #     print(text)
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return render_template('day.html')    #(url_for('download_file', name=filename))

    return redirect(request.url)


@app.route('/quiz', methods=['POST', 'GET'])
def quiz():
    if request.method == 'POST':
        growth = request.form.get('growth')
        weight = request.form.get('weight')
        date_birth = request.form.get('date_birth')
        hand = request.form.get('hand')
        thorax = request.form.get('thorax')
        waist = request.form.get('waist')
        abdomen = request.form.get('abdomen')
        buttocks = request.form.get('buttocks')
        thigh = request.form.get('thigh')
        print(growth,weight, date_birth, hand, thorax, waist, abdomen, buttocks, thigh)
        flash('Отлично!', category='right')
    return redirect(url_for('day_marathon', day_number='0'))


# @app.route('/admin', methods=['POST', 'GET'])
# @login_required
# def admin():
#     print('PRIVET')
#     if current_user.is_authenticated and current_user.role == 'admin':
#         print(request.url)
#         return render_template('admin/master.html')
#         # return render_template('admin/master.html')
#     else:
#         return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page404.html', title='Старница не найдена')