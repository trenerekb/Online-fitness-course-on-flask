from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

# LoginManager
manager = LoginManager()
manager.login_view = 'registration.login'
manager.init_app(app)
