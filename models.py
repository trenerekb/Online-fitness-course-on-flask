from datetime import datetime

from flask_login import UserMixin

from app import db, manager


# МИГРАЦИ В БД
# Обновление через терминал:
# set FLASK_APP=app.py
# flask db migrate
# flask db upgrade
# (если не сработало, то - flask db stamp head перед migrate)

# Создание таблиц через Console:
# from app import db
# import models
# db.create.all()


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

    reports = db.relationship('Report', back_populates='clients', lazy=True)
    results = db.relationship('Result', backref='client', lazy=True)
    comments = db.relationship('Comment', cascade='all,delete', back_populates='clients', lazy=True)
    likes = db.relationship('Like', cascade='all,delete', backref='client', lazy=True)
    body_photos = db.relationship('BodyPhoto', cascade='all,delete', backref='client', lazy=True)
    profiles = db.relationship('Profile', cascade='all,delete', backref='client', lazy=True)

    def __repr__(self):
        return f'<Client {self.id}, {self.name} {self.surname}>'


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'), nullable=False)
    text = db.Column(db.Text)
    # like = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.now())

    images = db.relationship('Image', cascade='all,delete', backref='report', lazy=True)
    clients = db.relationship('Client', back_populates='reports', lazy=True)
    comments = db.relationship('Comment', cascade='all,delete', backref='report', lazy=True)
    likes = db.relationship('Like', cascade='all,delete', backref='report', lazy=True)

    def __repr__(self):
        return f'<Report {self.id}, client_id {self.client_id}, day_id {self.day_id}>'


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __repr__(self):
        return f'<Like {self.id}, report_id {self.id}, client_id {self.id}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.now())

    clients = db.relationship('Client', back_populates='comments', lazy=True)

    def __repr__(self):
        return f'<Comment {self.id}>, report_id {self.id}, client_id {self.id}>'


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_day = db.Column(db.Integer)
    video_path = db.Column(db.String)
    resume_video = db.Column(db.Text)
    cover_video_path = db.Column(db.String)
    title_video = db.Column(db.String(500))
    task_description = db.Column(db.Text)

    reports = db.relationship('Report', backref='day', lazy=True)
    results = db.relationship('Result', backref='day', lazy=True)

    def __repr__(self):
        return f'Day {self.number_day}'


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    image_path = db.Column(db.String)

    def __repr__(self):
        return f'<ImageReport {self.id}, report_id {self.report_id}, image_path {self.image_path}>'


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    weight = db.Column(db.Float)
    growth = db.Column(db.Float)
    hand = db.Column(db.Float)
    thorax = db.Column(db.Float)
    waist = db.Column(db.Float)
    abdomen = db.Column(db.Float)
    buttocks = db.Column(db.Float)
    thigh = db.Column(db.Float)
    shin = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Result {self.id}, day_id {self.day_id}>'


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    avatar_client = db.Column(db.String)

    def __repr__(self):
        return f'<Profile {self.id}>, client_id {self.client_id}>, avatar_client {self.avatar_client}>'


class BodyPhoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    before_photos = db.Column(db.String)
    after_photos = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<BodyPhoto {self.id}>, ' \
               f'client_id {self.client_id}>, ' \
               f'before_photos {self.before_photos}, ' \
               f'after_photos {self.after_photos}, ' \
               f'day_id {self.day_id}>'


@manager.user_loader
def load_user(user_id):
    return Client.query.get(user_id)


