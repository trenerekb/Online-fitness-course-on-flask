import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from werkzeug.utils import secure_filename
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


def index():
    # print(url_for('index'))
    return redirect(url_for('/login'))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Configuration.ALLOWED_EXTENSIONS

# @app.route('/about')
# def about():
#     print(url_for('about'))
#     return render_template('about.html', title='О сайте', menu=menu)
#
#
# @app.route('/contact', methods=['POST', 'GET'])
# def contact():
#     if request.method == 'POST':
#         if len(request.form['username']) > 2:
#             flash('Сообщение отправлено', category='success')
#         else:
#             flash('Ошибка отправки', category='error')
#
#     return render_template('contact.html', title='Обратная связь', menu=menu)

@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    # print(request.form)
    # if 'userLogged' in session:
    #     return redirect(url_for('profile', username=session['userLogged']))
    if request.method == 'POST' and request.form['username'] == 'trener_ekb@rambler.ru' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
        # if len(request.form['psw']) < 2:
        #     flash('Отправлено', category='success')
    else:
        flash('Ошибка email или пароля', category='error')

    return render_template('login.html', title='Авторизация')


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template('profile.html', title='Профиль', username=username)
    # return f'Профиль пользователя: {username}'


@app.route('/day/<day_number>')
def get_day_marathon(day_number):
    current_user = 'Ruslan G'
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
        header = 'День 0'
        return render_template('day.html', title=header, video=video, video_title = video_title, header=header,
                               task_description=task_description, current_user=current_user,
                               user_name_comment=user_name_comment, date_comment=date_comment, comment=comment,
                               user_name_reply=user_name_reply, date_reply_comment=date_reply_comment,
                               reply_comment=reply_comment, text_report_current_user=text_report_current_user,
                               date_report_current_user=date_report_current_user)
    elif day_number == '1':
        header = 'День 1'
        return render_template('day.html', title=header, video_title = video_title, header=header,
                               task_description=task_description)

    return render_template('profile.html', title='Профиль')


@app.route('/user_comment')
def get_user_comment():
    pass
    # comment = User.get_сomment()


@app.route('/add_report', methods=['POST', 'GET'])
def add_report():
    if request.method == 'POST':
        text = request.form['text_report']
        print(text)
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


    # if request.method == 'POST':
    #     # images = request.form['images_report']
    #     text = request.form['text_report']
    #     img = request.files['file']
    #     # img_name = img.filename
    #     print(text)
    #     # img.save('static/images', img_name)
    #     return render_template('day.html', title='Старница не найдена')


@app.errorhandler(404)
def page_not_fount(error):
    return render_template('page404.html', title='Старница не найдена')


if __name__ == "__main__":
    app.run()