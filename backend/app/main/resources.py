import datetime as dt
from flask import jsonify, url_for
from flask_restful import Resource, reqparse
from app.models import Map


class MapResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        self.parser.add_argument('status', type=int, location='args')
        args = self.parser.parse_args()

        maps = Map.query
        response = jsonify(maps.all())
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

