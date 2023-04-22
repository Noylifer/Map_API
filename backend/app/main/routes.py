from app.main import api
from app.main.resources import MapResource

api.add_resource(MapResource, '/map')
