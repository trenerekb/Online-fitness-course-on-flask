from flask import redirect, url_for
from flask_admin import BaseView, expose


class ExitView(BaseView):
    @expose('/')
    def index2(self):
        return redirect(url_for("registration.login"))