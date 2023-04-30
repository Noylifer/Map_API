import app
from app.main import api
from app.main.resources import MapResource
from app.main import bp
from app.models import Admin, Map
from flask_login import login_user, logout_user, current_user
from flask import url_for, send_from_directory, send_file, redirect, request, render_template, jsonify, current_app, after_this_request
from os import path
import os
from flask_cors import cross_origin, CORS

CORS(bp)


@bp.route('/')
def main():
    return redirect(url_for('main.login'))

@bp.route('/map', methods=["GET"])
@cross_origin()
def api():
    @after_this_request
    def add_header(response):
        response.headers.add("X-Frame-Options", "*")
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    maps = Map.query
    response = jsonify(maps.all())
    return response



@bp.route('/static/<path>', methods=['GET'])
def send_report(path):
    try:
        return send_file(os.getcwd() + '\\app\\static\\' + path +'.png')
    except:
        return 'Not find'

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('admin')

    if request.method == 'POST':
        admin = Admin.query.filter_by(username=request.form.get('login').lower()).first()
        if admin is None or not admin.check_password(request.form.get('password')):
            return redirect(url_for('main.login'))

        login_user(admin, remember=True)
        return redirect('admin')

    return render_template('admin/login.html', title='Авторизация')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
