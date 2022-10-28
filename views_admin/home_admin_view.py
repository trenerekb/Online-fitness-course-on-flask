from flask_admin import AdminIndexView, expose
from flask_login import login_required, current_user
from flask import url_for, redirect


class HomeAdminView(AdminIndexView):
    @expose('/')
    @login_required
    def admin_home(self):
        if current_user.is_authenticated and current_user.role == 'admin':
            return self.render('admin/index.html')

        return redirect(url_for('login'))
