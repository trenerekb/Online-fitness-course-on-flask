from flask_admin import Admin

from admin.client_view import ClientView
from admin.day_view import DayView
from admin.exit_view import ExitView
from admin.home_admin_view import HomeAdminView
from admin.report_view import ReportView
from app import app, db
from models import Client, Day, Report

admin = Admin(app, 'Body Home', template_mode='bootstrap4', index_view=HomeAdminView(), url='/')

admin.add_view(ClientView(Client, db.session))
admin.add_view(DayView(Day, db.session))
admin.add_view(ReportView(Report, db.session))
admin.add_view(ExitView(name='Выход', url='exit'))

