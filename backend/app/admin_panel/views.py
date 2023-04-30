import os
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import UserMixin, current_user, login_user, logout_user
from app.models import Admin
from flask import redirect, url_for
from app import login
from flask_admin.menu import MenuLink
file_path = os.path.abspath(os.path.dirname(__name__))


class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated

@login.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.login'))


class MapView(MyModelView):
    column_labels = {
        'number': 'Номер участка',
        'square': 'Площадь',
        'available': 'Доступность для покупки',
    }

    # поля формы создания и редактирования
    form_columns = ('number', 'square', 'available')

    # поля вывода
    column_list = ('number', 'square', 'available')

    column_editable_list = ('number', 'square', 'available')
    column_default_sort = ('number', True)
    column_searchable_list = ['number', 'available']

    export_max_rows = 500
    export_types = ['csv']
    form_widget_args = {
        'date': {
            'style': 'max-width: 200px;'
        },
    }
    create_template = 'admin/map_create.html'
    edit_template = 'admin/map_edit.html'

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

