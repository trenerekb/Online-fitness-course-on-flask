from flask_admin.contrib.sqla import ModelView


class ClientView(ModelView):
    # Список отображаемых колонок
    column_list = ['name', 'surname', 'role', 'phone', "email", "psw", "date_birth", "date"]

    # Называние отображаемых колонок при редактировании
    column_labels = {
        'name': 'Имя',
        'surname': "Фамилия",
        'role': "Роль",
        'phone': "Телефон",
        "email": "Почта",
        "psw": "Пароль",
        "date_birth": "День рождения",
        "date": "Дата регистрации"}

    # Указываем колонки, в которых можно выставить сортировку
    column_sortable_list = ('name', 'surname', 'role', 'date', "date_birth")

    # Разрешаем экспорт в виде excel (но можно в другом формате - export_types = ['csv'])
    can_export = True

    # Создание выбора роли пользователя
    AVAILABLE_CLIENT_TYPES = [
        (u'admin', u'admin'), (u'author', u'author'), (u'student', u'student')
    ]

    form_choices = {'role': AVAILABLE_CLIENT_TYPES}

    # Скрываем поля
    column_exclude_list = ['psw']
    # Поиск по...
    column_searchable_list = ['surname', 'name', 'phone']
    # Редактирование полей
    column_editable_list = ['role', 'name', 'surname', 'phone', 'email', 'date', 'date_birth']
    # Исключаем поля в страницах редактирования и создания
    form_excluded_columns = ['profiles', 'reports', 'results']

    def create_form(self, obj=None):
        return super(ClientView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(ClientView, self).edit_form(obj)

    # def on_model_change(self, form, model, is_created):
    #     model.psw = generate_password_hash(model.psw)


