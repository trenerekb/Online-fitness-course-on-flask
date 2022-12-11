from flask_admin.contrib.sqla import ModelView


def name_gen_image(model, file_data):

    print(model.query.filter_by(client_id=model.client_id).first())
    hash_name = f'{model.client_id} {model.surname}/report_id-{model.id}/{file_data.filename}'
    return hash_name


class ImageView(ModelView):

    column_list = ['report_id', 'image_path']
    # column_list = [ f'{Client.surname} {Client.name}', Day.number_day, Image.image_path, 'text', "date"]

    # Называние отображаемых колонок при редактировании
    column_labels = {
        'report_id': "id Отчета",
        'image_path': "Путь к картинке",
    }
    #
    # form_extra_fields = {
    #     'cover_video_path': form.ImageUploadField('Загрузи фото отчета',
    #                                               # Передаем абсолютный путь к каталогу, где хранятся файлы
    #                                               base_path=os.path.join(Configuration.base_dir,
    #                                                                      'static/storage/reports/'),
    #                                               url_relative_path='storage/reports/',
    #                                               namegen=name_gen_image,
    #                                               allowed_extensions=['jpg', 'jpeg', 'png'],
    #                                               max_size=(525, 934, True))
    # }
    #
    # def _list_thumbnail(view, context, model, name):
    #     if not model.image_path:
    #         return ''
    #
    #     url = url_for('static', filename=os.path.join('storage/reports/', model.image_path))
    #
    #     if model.image_path.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg']:
    #         return Markup(f'<img src={url} width="100">')
    #
    # # Передаем в поле 'обложка видео' результат функции _list_thumbnail
    # column_formatters = {'cover_video_path': _list_thumbnail}

    def create_form(self, obj=None):
        return super(ImageView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(ImageView, self).edit_form(obj)