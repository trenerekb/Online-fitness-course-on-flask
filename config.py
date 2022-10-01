import os


class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'fdavbmeworvepz'
    MAX_CONTENT_LENGTH = 10240 * 10240
    UPLOAD_FOLDER = r'D:/Python/fitness_marathon/uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/users_data'
    #'mysql:///' + os.path.join(basedir, 'database.db')