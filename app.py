from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

# LoginManager
manager = LoginManager()
manager.login_view = 'login'
manager.init_app(app)

# ADMIN #
from models import Client, Day, Report
from views_admin.client_view import ClientView
from views_admin.day_view import DayView
from views_admin.report_view import ReportView
from views_admin.exit_view import ExitView
from views_admin.home_admin_view import HomeAdminView

admin = Admin(app, 'Body Home', template_mode='bootstrap4', index_view=HomeAdminView(), url='/')

admin.add_view(ClientView(Client, db.session))
admin.add_view(DayView(Day, db.session))
admin.add_view(ReportView(Report, db.session))
admin.add_view(ExitView(name='Выход', url='exit'))
