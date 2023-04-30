from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

bp = Blueprint('main', __name__)
CORS(bp)
api = Api()
api.init_app(bp)

from app.main import routes
