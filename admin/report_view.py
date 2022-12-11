from flask_admin.contrib.sqla import ModelView

from models import Client, Day, Image


class ReportView(ModelView):

    # column_list = ['Пользователь', 'day_id', 'text', "date"]
    column_list = [ 'client_id', 'day_id', 'text', "date"]

    # Называние отображаемых колонок при редактировании
    column_labels = {
        'client_id': "Пользователь",
        'day_id': "№ дня",
        'text': "Описание отчета",
        "date": 'Дата'
    }

    def create_form(self, obj=None):
        return super(ReportView, self).create_form(obj)

    def edit_form(self, obj=None):
        return super(ReportView, self).edit_form(obj)