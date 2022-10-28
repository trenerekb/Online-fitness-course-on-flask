import os.path

from flask import url_for, Markup
from flask_admin import form
from flask_admin.contrib.sqla import ModelView

# 'D:\Python\fitness_marathon'
file_path = os.path.abspath(os.path.dirname(__name__))


def name_gen_image(model, file_data):
    hash_name = f'day{model.number_day}/{file_data.filename}'
    return hash_name


def name_gen_video(model, file_data):
    hash_name = f'day{model.number_day}/{file_data.filename}'
    return hash_name


class DayView(ModelView):

    column_labels = {
    'number_day': '№ Дня',
    'video_path': 'Видео',
    'cover_video_path':'Обложка',
    'title_video': 'Название видео',
    'task_description': "Описание задания"
    }

    def _list_thumbnail_image(view, context, model, name):
        if not model.cover_video_path:
            return ''

        url = url_for('static', filename=os.path.join('storage/marathon_days/', model.cover_video_path))

        if model.cover_video_path.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg']:
            return Markup(f'<img src={url} width="100">')

    def _list_thumbnail_video(view, context, model, name):
        if not model.video_path:
            return ''

        url = url_for('static', filename=os.path.join('storage/marathon_days/', model.video_path))

        if model.video_path.split('.')[-1] in ['mp4']:
            return Markup(f'<video width="200" height="150" controls="controls">'
                          f'<source src={url} type="audio/mpeg"/></video>')

    # Передаем в поля с изображениями и видео результат функций
    column_formatters = {'cover_video_path': _list_thumbnail_image, 'video_path': _list_thumbnail_video}

    # Формируем загрузочные поля при создании и редактировании
    form_extra_fields = {
        'cover_video_path': form.ImageUploadField('Загрузи обложку для видео',
                                                  # Передаем абсолютный путь к каталогу, где хранятся файлы
                                                  base_path=os.path.join(file_path,
                                                  'static/storage/marathon_days/'),
                                                  url_relative_path='storage/marathon_days/',
                                                  namegen=name_gen_image,
                                                  allowed_extensions=['jpg', 'jpeg', 'png']),
        'video_path': form.FileUploadField('Загрузи видео', base_path=os.path.join(file_path,
                                           f'static/storage/marathon_days/'),
                                           namegen=name_gen_image,
                                           allowed_extensions=['mp4'])
    }

    # Исключаем поля в страницах редактирования и создания
    form_excluded_columns = ['reports']

    def create_form(self, obj=None):
        return super(DayView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(DayView, self).edit_form(obj)