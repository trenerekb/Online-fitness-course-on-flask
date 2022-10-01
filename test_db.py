from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/users_data'
# app.config.from_object(Configuration)

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.now())

    # def __int__(self, *args, **kwargs):
    #     super(Users, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Users {self.id}>'


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users_id'))

    # def __int__(self, *args, **kwargs):
    #     super(Profiles, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Profiles {self.id}>'
# try:
#     connection = pymysql.connect(
#         host='localhost',
#         port=8889,
#         user='root',
#         password='',
#         database='users_data',
#         cursorclass=pymysql.cursors.DictCursor,
#         autocommit=True
#     )
#     print('Good....')
# except Exception as ex:
#     print('Bad...')
#     print(ex)