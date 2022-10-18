

class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'fdav54bmkhjbhjewor123vepz'
    MAX_CONTENT_LENGTH = 10240 * 10240
    UPLOAD_FOLDER = r'D:/Python/fitness_marathon/uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///women_marathon.db'
    #'mysql:///' + os.path.join(basedir, 'database.db')