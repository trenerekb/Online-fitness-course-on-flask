from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate()

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

# LoginManager
manager = LoginManager()
manager.login_view = 'registration.login'
manager.init_app(app)

# Admin
from flask_admin import Admin

from admin.client_view import ClientView
from admin.day_view import DayView
from admin.exit_view import ExitView
from admin.home_admin_view import HomeAdminView
from models import Client, Day, Report, Image
from admin.report_view import ReportView
from admin.image_view import ImageView

admin = Admin(app, 'Body Home', template_mode='bootstrap4', index_view=HomeAdminView(), url='/')

admin.add_view(ClientView(Client, db.session))
admin.add_view(DayView(Day, db.session))
admin.add_view(ReportView(Report, db.session))
admin.add_view(ImageView(Image, db.session))
# admin.add_view(ResultView(Result, db.session))
admin.add_view(ExitView(name='Выход', url='exit'))
