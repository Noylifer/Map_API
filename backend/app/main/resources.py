import datetime as dt
from flask import jsonify
from flask_restful import Resource, reqparse
from app.models import Map


class MapResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument('status', type=int, location='args')
        args = self.parser.parse_args()

        maps = Map.query

        return jsonify(maps.all())
