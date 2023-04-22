# from app import db
# from flask import url_for, redirect, current_app
# from app.models import Admin, Map
# from app.admin_panel.views import MapView
# # flask-login
# from flask_login import current_user
# import flask_login as login
#
# # flask-security
# from flask_security import SQLAlchemyUserDatastore, Security
#
# # flask-admin
# # import flask_admin
# # from flask_admin import helpers, expose
#
# # Setup Flask-Security
# user_datastore = SQLAlchemyUserDatastore(db, Admin,)
# security = Security(current_app, user_datastore)
#
#
# # Переадресация страниц (используется в шаблонах)
# class MyAdminIndexView(flask_admin.AdminIndexView):
#     @expose('/')
#     def index(self):
#         if not current_user.is_authenticated:
#             return redirect(url_for('.login_page'))
#         return super(MyAdminIndexView, self).index()
#
#     @expose('/login/', methods=('GET', 'POST'))
#     def login_page(self):
#         if current_user.is_authenticated:
#             return redirect(url_for('.index'))
#         return super(MyAdminIndexView, self).index()
#
#     @expose('/logout/')
#     def logout_page(self):
#         login.logout_user()
#         return redirect(url_for('.index'))
#
#
# # Create admin
# admin = flask_admin.Admin(current_app, index_view=MyAdminIndexView(), base_template='admin/master-extended.html')
#
# # Add view
# admin.add_view(MapView(Map, db.session, name="Данные участков"))
#
#
# # define a context processor for merging flask-admin's template context into the
# # flask-security views.
# @security.context_processor
# def security_context_processor():
#     return dict(
#         admin_base_template=admin.base_template,
#         admin_view=admin.index_view,
#         h=helpers,
#         get_url=url_for
#     )