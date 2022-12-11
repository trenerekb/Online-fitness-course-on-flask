import os
import re
import shutil
from datetime import datetime

from PIL import Image
from werkzeug.utils import secure_filename

from app import app
from config import Configuration


class ImageHandler:

    def image_compression(self, file):
        img = Image.open(file)
        if img.__sizeof__() > 150:
            height, width = (img.height // 2, img.width // 2)
            img_resized = img.resize((width, height))
            return img_resized
        return img

    def get_path_to_user_folder(self, client_id):
        path_to_user_report = os.path.join(app.config['UPLOAD_FOLDER'], str(client_id))
        return path_to_user_report

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Configuration.ALLOWED_EXTENSIONS

    def get_secure_name_file(self, file):
        file_name = secure_filename(datetime.now().__str__() + '_' + file.filename)
        return file_name

    def name_image_check(self, file):
        return False if file.filename == '' else True

    def validation_file(self, file):
        if self.name_image_check(file):
            if self.allowed_file(file.filename):
                return True
            else:
                return False, "Файл не содержит подходящего расширения"
        else:
            return False, 'Файл не прикреплен'

    def creating_secure_path(self, path_to_user_report, path_to_day_number):
        try:
            if os.path.exists(path_to_user_report):
                if os.path.exists(path_to_day_number):
                    folder_path = path_to_day_number
                    return folder_path
                else:
                    os.makedirs(path_to_day_number, exist_ok=True)
                    folder_path = path_to_day_number
                    return folder_path
            else:
                os.makedirs(path_to_day_number, exist_ok=True)
                folder_path = path_to_day_number
                return folder_path
        except Exception:
            return False, 'Ошибка при создании пути к папке'

    def save_image(self, file, day_number, client_id):
        try:
            file_name = self.get_secure_name_file(file)
            path_to_user_report = self.get_path_to_user_folder(client_id)
            path_to_day_number = os.path.join(path_to_user_report, f'day{day_number}')

            folder_path = self.creating_secure_path(path_to_user_report, path_to_day_number)
            if folder_path:
                img = self.image_compression(file)
                try:
                    img.save(os.path.join(folder_path, file_name))
                    path_to_image = os.path.join(folder_path, file_name)
                    try:
                        path_to_image = re.sub(r'\\', '/', path_to_image)
                        path_to_image = path_to_image[path_to_image.find('/storage'):]
                        return path_to_image
                    except:
                        return False, 'Ошибка при редактировании имени пути к файлу'
                except ValueError:
                    return False, f'Ошибка формата файла {file.filename}'
                except OSError:
                    return False, f'Файл {file.filename} не может быть записан'
        except:
            return False, f'Ошибка при сохранении файла {file.filename}'

    def delete_folder_images(self, client_id: str, number_day: str):
        try:
            path_to_client_folder_images = os.path.join(app.config['UPLOAD_FOLDER'], client_id, f'day{number_day}')
            shutil.rmtree(path_to_client_folder_images)
            return True
        except:
            return False
