from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

manager = LoginManager(app)


