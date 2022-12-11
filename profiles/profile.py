from flask import Blueprint, url_for, request, flash, redirect, render_template
from flask_login import current_user, login_required

from app import db
from config import Configuration
from models import Report, Image, Day, Result, Profile, BodyPhoto, Client
from reports.image_handler import ImageHandler


profile = Blueprint('profiles', __name__, template_folder='templates')


@profile.route('/')
@login_required
def profile_view():
    number_days_in_marathon = [i for i in range(int(Day.query.count()))]
    day = Day.query.filter_by(id=1).first()
    client_id = current_user.id
    client_data = Client.query.filter(Client.id == client_id).first()

    return render_template('profiles/profile.html', title='Профиль', count_days=number_days_in_marathon,
                           client_data=client_data, day=day)


@profile.route('/avatar', methods=['POST'])
def update_avatar_user():
    if request.method == 'POST':
        file = request.files['file']

        if file:
            client_id = current_user.id
            img_hand = ImageHandler()

            if img_hand.validation_file(file):
                path_to_image = img_hand.save_image(file, '0', client_id)
                if path_to_image is None:
                    flash('Не удалось сохранить фото', category='error')
                    return redirect(url_for('.profile_view'))

                avatar_client = Profile.query.filter(Profile.client_id == client_id).first()
                if avatar_client:
                    avatar_client.avatar_client = path_to_image
                    db.session.commit()
                else:
                    new_avatar = Profile(client_id=client_id, avatar_client=path_to_image)
                    db.session.add(new_avatar)
                    db.session.commit()

            else:
                flash(img_hand.validation_file(file), category='error')
                return redirect(url_for('.profile_view'))

        return redirect(url_for('.profile_view'))

    return redirect(request.url)