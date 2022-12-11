from flask import Blueprint, url_for, request, flash, redirect, jsonify
from flask_login import current_user

from app import db
from models import Report, Image, Like, Comment
from reports.image_handler import ImageHandler

report = Blueprint('reports', __name__, template_folder='templates')


@report.route('/add/<day_number>', methods=['POST', 'GET'])
def add_report(day_number):
    if request.method == 'POST':
        if len(request.form['text_report']) < 10:
            flash('Текст вашего отчета менее 10 букв', category='error')
            return redirect(url_for('days.day_marathon', day_number=day_number))

        text = request.form['text_report']
        files = request.files.getlist('file')

        client_id = current_user.id
        new_report = Report(client_id=client_id, day_id=day_number, text=text)
        db.session.add(new_report)
        db.session.flush()

        report_id = new_report.id

        for file in files:
            img_hand = ImageHandler()

            if img_hand.validation_file(file):
                path_to_image = img_hand.save_image(file, day_number, client_id)
                if path_to_image is None:
                    flash('Не удалось сохранить фото', category='error')
                    return redirect(url_for('days.day_marathon', day_number=day_number))

                new_image = Image(report_id=report_id, image_path=path_to_image)
                db.session.add(new_image)

            else:
                flash(img_hand.validation_file(file), category='error')
                return redirect(url_for('days.day_marathon', day_number=day_number))

        db.session.commit()

        flash('Отчет добавлен', category='right')
        return redirect(url_for('days.day_marathon', day_number=day_number))

    return redirect(request.url)


@report.route('/del/<day_number>', methods=['POST', 'GET'])
def delete_report(day_number):
    if request.method == 'POST':
        client_id = current_user.id
        client_report = Report.query.filter(Report.client_id == client_id, Report.day_id == day_number).first()

        if client_report:
            img_hand = ImageHandler()
            img_hand.delete_folder_images(client_id=str(client_id), number_day=str(day_number))
            try:
                db.session.delete(client_report)
                db.session.commit()
            except:
                db.session.rollback()

        return redirect(url_for('days.day_marathon', day_number=day_number))

    return redirect(url_for('days.day_marathon', day_number=day_number))


@report.route('/update/<day_number>', methods=['POST', 'GET'])
def update_report(day_number):
    if request.method == 'POST':
        if len(request.form['text_report']) < 10:
            flash('Текст вашего отчета менее 10 букв', category='error')
            return redirect(url_for('days.day_marathon', day_number=day_number))

        text = request.form['text_report']
        new_files = request.files.getlist('file')
        form_data = request.form

        client_id = current_user.id
        client_report = Report.query.filter(Report.client_id == client_id, Report.day_id == day_number).first()

        client_report.text = text

        for image in client_report.images:
            if image.image_path not in form_data:
                db.session.delete(image)
                db.session.flush()
        report_id = client_report.id

        for file in new_files:
            if file:
                img_hand = ImageHandler()

                if img_hand.validation_file(file):
                    path_to_image = img_hand.save_image(file, day_number, client_id)
                    if path_to_image[0] is False:
                        flash(path_to_image[1], category='error')
                        return redirect(url_for('days.day_marathon', day_number=day_number))

                    new_image = Image(report_id=report_id, image_path=path_to_image)
                    db.session.add(new_image)
                    db.session.flush()

                else:
                    flash(img_hand.validation_file(file)[1], category='error')
                    return redirect(url_for('days.day_marathon', day_number=day_number))
        try:
            db.session.commit()

            flash('Отчет добавлен', category='right')
            return redirect(url_for('days.day_marathon', day_number=day_number))
        except:
            db.session.rollback()
            flash('Ошибка при добавлении в базу', category='right')
            return redirect(url_for('days.day_marathon', day_number=day_number))

    return redirect(request.url)


@report.route('/like/<report_id>', methods=['POST'])
def like(report_id):
    client_id = current_user.id
    like_report = Like.query.filter(Like.client_id == client_id, Like.report_id == report_id).first()

    if like_report:
        db.session.delete(like_report)
        db.session.commit()

    else:
        new_like = Like(client_id=client_id, report_id=report_id)
        db.session.add(new_like)
        db.session.commit()

    report = Report.query.filter(Report.id == report_id).first()
    number_likes = len(report.likes)
    bool_liked = client_id in map(lambda x: x.client_id, report.likes)

    return jsonify({"likes": number_likes, "liked": bool_liked})


# WORKING WITH COMMENTS TO THE REPORTS
@report.route('/add_comment/<report_id>/<day_number>', methods=['POST'])
def add_comment_to_report(report_id, day_number):
    text = request.form['text_comment']

    new_comment = Comment(client_id=current_user.id, report_id=report_id, text=text)
    try:
        db.session.add(new_comment)
        db.session.commit()
    except:
        db.session.rollback()
        return redirect(url_for('days.day_marathon', day_number=day_number))

    return redirect(url_for('days.day_marathon', day_number=day_number))


@report.route('/del_comment/<comment_id>/<day_number>', methods=['GET'])
def delete_comment(comment_id, day_number):
    comment = Comment.query.filter(Comment.id == comment_id).first()
    if comment:
        try:
            db.session.delete(comment)
            db.session.commit()
        except:
            db.session.rollback()
            return redirect(url_for('days.day_marathon', day_number=day_number))

    return redirect(url_for('days.day_marathon', day_number=day_number))
