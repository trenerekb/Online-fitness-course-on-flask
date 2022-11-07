import os

from flask import Blueprint, render_template, url_for, request, flash, session, redirect, abort
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename

from app import db, app
from config import Configuration
from models import Client


report = Blueprint('report', __name__, template_folder='templates')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Configuration.ALLOWED_EXTENSIONS


@report.route('/<day_number>', methods=['POST', 'GET'])
def add_report(day_number):
    if request.method == 'POST':
        if len(request.form['text_report']) < 10:
            flash('Текст вашего отчета менее 10 букв', category='error')
            return redirect(url_for('day_marathon', day_number=day_number))

        text = request.form['text_report']
        files = request.files.getlist('file')

        for file in files:
            if file.filename == '':
                flash('Вы не прикрепили фото', category='error')
                return redirect(url_for('day_marathon', day_number=day_number))

            if file and allowed_file(file.filename):
                print(file.filename)
                file_name = secure_filename(file.filename)
                path_to_user_report = os.path.join(app.config['UPLOAD_FOLDER'], str(current_user.id))

                if os.path.exists(path_to_user_report):
                    if os.path.exists(path_to_user_report+f'/day{day_number}'):
                        file.save(os.path.join(path_to_user_report + f'/day{day_number}', file_name))
                    else:
                        os.makedirs(path_to_user_report + f'/day{day_number}', exist_ok=True)
                        file.save(os.path.join(path_to_user_report + f'/day{day_number}', file_name))
                else:
                    os.makedirs(path_to_user_report+f'/day{day_number}', exist_ok=True)
                    file.save(os.path.join(path_to_user_report + f'/day{day_number}', file_name))

        flash('Отчет добавлен', category='right')
        return redirect(url_for('day_marathon', day_number=day_number))

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