import os


class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'fdav54bmkhjbhjewor123vepz'
    MAX_CONTENT_LENGTH = 10240 * 10240
    UPLOAD_FOLDER = r'D:/Python/fitness_marathon/static/storage/reports/'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'jfif'}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///women_marathon.db'     # ?check_same_thread=False

    # Путь до папки с хранением видео и обложек
    path_to_video_and_cover = 'storage/marathon_days/'
    # 'D:\Python\fitness_marathon'
    base_dir = os.path.abspath(os.path.dirname(__file__))

    avatar_default = ['/storage/avatar_default/pic-1.jpg',
                      '/storage/avatar_default/pic-2.jpg',
                      '/storage/avatar_default/pic-3.jpg']

    # permanent_session_lifetime = datetime.timedelta(days=35)
    #'mysql:///' + os.path.join(basedir, 'database.db')