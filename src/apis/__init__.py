from flask import Flask
from configs import ApplicationConfig


app = Flask(ApplicationConfig.NAME)

class HTTP:
    class METHOD:
        DELETE = 'delete'
        PATCH = 'patch'
        PUT = 'put'
        POST = 'post'
        GET = 'get'

    class STATUS:
        OK = 200

class URI:
    LIGHT_PING = '/light/ping'
    LIGHTS_IN_ROOM = '/light/lights-in-room/<room_id>'

