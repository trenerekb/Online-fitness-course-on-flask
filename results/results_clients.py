from datetime import datetime

from flask import Blueprint, url_for, request, flash, redirect
from flask_login import current_user

from app import db
from models import Result, Client, BodyPhoto
from reports.image_handler import ImageHandler

result = Blueprint('results', __name__)


@result.route('/<day_number>', methods=['POST', 'GET'])
def record_results(day_number):
    if request.method == 'POST':
        weight = request.form.get('weight')
        hand = request.form.get('hand')
        thorax = request.form.get('thorax')
        waist = request.form.get('waist')
        abdomen = request.form.get('abdomen')
        buttocks = request.form.get('buttocks')
        thigh = request.form.get('thigh')
        shin = request.form.get('shin')

        client_id = current_user.id

        if day_number == '0':
            growth = request.form.get('growth')
            date_birth = request.form.get('date_birth')
            before_photos = request.files.getlist('file')

            new_result = Result(client_id=client_id, day_id=day_number, growth=growth, weight=weight,
                                hand=hand, thorax=thorax, waist=waist, abdomen=abdomen,
                                buttocks=buttocks, thigh=thigh, shin=shin)
            client = Client.query.filter(Client.id == client_id).first()
            client.date_birth = datetime.strptime(date_birth, "%Y-%m-%d")
            db.session.add(new_result)
            db.session.flush()

            for file in before_photos:
                img_hand = ImageHandler()

                if img_hand.validation_file(file):
                    path_to_image = img_hand.save_image(file, day_number, client_id)
                    if path_to_image is None:
                        flash('Не удалось сохранить фото', category='error')
                        return redirect(url_for('days.day_marathon', day_number=day_number))

                    new_image = BodyPhoto(client_id=client_id, day_id=day_number, before_photos=path_to_image)
                    db.session.add(new_image)

                else:
                    flash(img_hand.validation_file(file), category='error')
                    return redirect(url_for('days.day_marathon', day_number=day_number))

            db.session.commit()
            flash('Отчет добавлен! Переходите на следующий день', category='right')
            redirect(url_for('days.day_marathon', day_number=day_number))

        if day_number in ('7', '14'):
            new_result = Result(client_id=client_id, day_id=day_number, weight=weight,
                                hand=hand, thorax=thorax, waist=waist, abdomen=abdomen,
                                buttocks=buttocks, thigh=thigh, shin=shin)

            db.session.add(new_result)

            db.session.commit()
            flash('Отчет добавлен! Переходите на следующий день', category='right')
            redirect(url_for('days.day_marathon', day_number=day_number))

    return redirect(url_for('days.day_marathon', day_number=day_number))