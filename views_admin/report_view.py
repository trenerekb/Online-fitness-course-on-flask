import os.path

from flask import url_for, Markup
from flask_admin import form
from flask_admin.contrib.sqla import ModelView

from models import Image, Client, Day


# 'D:\Python\fitness_marathon'
file_path = os.path.abspath(os.path.dirname(__name__))


def name_gen_image(model, file_data):

    print(model.query.filter_by(client_id=model.client_id).first())
    hash_name = f'{model.client_id} {model.surname}/report_id-{model.id}/{file_data.filename}'
    return hash_name


class ReportView(ModelView):

    column_list = ['Пользователь', 'day_id', 'image_path', 'text', "date"]
    # column_list = [ f'{Client.surname} {Client.name}', Day.number_day, Image.image_path, 'text', "date"]

    # Называние отображаемых колонок при редактировании
    column_labels = {
        'client_id': "Пользователь",
        'day_id': "№ дня",
        'image_path': 'Фото',
        'text': "Описание отчета",
        "date": 'Дата'
    }

    form_extra_fields = {
        'cover_video_path': form.ImageUploadField('Загрузи фото отчета',
                                                  # Передаем абсолютный путь к каталогу, где хранятся файлы
                                                  base_path=os.path.join(file_path,
                                                                         'static/storage/reports/'),
                                                  url_relative_path='storage/reports/',
                                                  namegen=name_gen_image,
                                                  allowed_extensions=['jpg', 'jpeg', 'png'],
                                                  max_size=(525, 934, True))
    }

    def _list_thumbnail(view, context, model, name):
        if not model.image_path:
            return ''

        url = url_for('static', filename=os.path.join('storage/reports/', model.image_path))

        if model.image_path.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg']:
            return Markup(f'<img src={url} width="100">')

    # Передаем в поле 'обложка видео' результат функции _list_thumbnail
    column_formatters = {'cover_video_path': _list_thumbnail}

    def create_form(self, obj=None):
        return super(ReportView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(ReportView, self).edit_form(obj)