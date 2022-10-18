from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL
# from flask_mysql_connector import MySQL
from flask import Flask
import pymysql


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'fdavbmeworvepz'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'users_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ruslan:bararus451@127.0.0.1/users_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/postgres'
# app.config.from_object(Configuration)

db = SQLAlchemy(app)
# db = sqlalchemy.create_engine('mysql+pymysql://root:1@127.0.0.1/users_data')


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

    def __int__(self, *args, **kwargs):
        super(Profiles, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Profiles {self.id}>'

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)












# import pymysql.cursors
#
# try:
#     connection = pymysql.connect(host='localhost',
#                                  user='ruslan',
#                                  password='bararus451',
#                                  database='sakila',
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor)
#     try:
#         with connection:
#             with connection.cursor() as cursor:
#                 # Create a new record
#                 sql = "SELECT * FROM actor;"
#                 cursor.execute(sql)
#                 rows = cursor.fetchall()
#                 for row in rows:
#                     print(row)
#                 print('#' * 20)
#
#     finally:
#         connection.close()
#
# except Exception as ex:
#     print(ex)
