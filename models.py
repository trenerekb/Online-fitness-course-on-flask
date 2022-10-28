from datetime import datetime

from flask_login import UserMixin

from app import db, manager


class Client(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='student')
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=False)
    date_birth = db.Column(db.DateTime)
    date = db.Column(db.DateTime, default=datetime.now())

    reports = db.relationship('Report', backref='client', lazy=True)
    profiles = db.relationship('Profile', backref='client', lazy=True)
    results = db.relationship('Result', backref='client', lazy=True)

    def __repr__(self):
        return f'<Client {self.id}, {self.name} {self.surname}>'


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    weight_start = db.Column(db.Float)
    growth = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Profile {self.id}>'


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    weight = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Result {self.id}>'


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_day = db.Column(db.Integer)
    video_path = db.Column(db.String)
    cover_video_path = db.Column(db.String)
    title_video = db.Column(db.String(500))
    task_description = db.Column(db.Text)

    reports = db.relationship('Report', backref='day', lazy=True)

    def __repr__(self):
        return f'Day {self.number_day}'


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'), nullable=False)
    text = db.Column(db.Text)
    like = db.Column(db.Integer)

    image = db.relationship('Image', backref='report', lazy=True)

    def __repr__(self):
        return f'<Report {self.id}>'


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    image_path = db.Column(db.String)

    def __repr__(self):
        return f'<ImageReport {self.id}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    text = db.Column(db.Text)

    def __repr__(self):
        return f'<Comment {self.id}>'


@manager.user_loader
def load_user(user_id):
    return Client.query.get(user_id)



