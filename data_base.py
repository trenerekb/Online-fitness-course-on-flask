from datetime import datetime
from app import db


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