import math
import time


class User:

    def from_db(self, user_id, db):
        self.__user =  {'name': 'Ruslan4ik', 'id': '123', 'comment': 'Hello word', 'time': '21-09-2022'} #db.getUser(user_id)


    def get_name(self):
        return self.__user['name'] if self.__user else 'Без имени'

    def get_avatar(self):
        return self.__user['name'] if self.__user else 'Без имени'

    def get_date(self):
        return self.__user['time'] if self.__user else 'Без даты'

    def get_сomment_user(self):
        return self.__user['comment'] if self.__user else 'Без комментария'

    def add_report(self, images, text):
        pass
        # try:
        #     time_report = math.floor(time.time())
        #     self.cu
        #
        # if request.method == 'POST':
        #     images = request.form['images_report']
        #     text = request.form['text_report']
        #     img = request.files['file']
        #     img_name = img.filename
        #     print(img_name, images, text)