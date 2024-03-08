from flask import Blueprint
from src.apis import URI, HTTP
from src.controllers.light_controller import LightsControlller
from flask import jsonify

light_mod = Blueprint("light_service", __name__)

@light_mod.route(URI.LIGHT_PING, methods=[HTTP.METHOD.GET])
def ping():
    return LightsControlller().ping()
    