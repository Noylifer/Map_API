from flask import Blueprint
from flask_restful import Api

bp = Blueprint('main', __name__)
api = Api()
api.init_app(bp)

from app.main import routes
