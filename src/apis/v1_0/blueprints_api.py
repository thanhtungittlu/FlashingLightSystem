from src.apis.v1_0.light import light_mod
from src.apis import app

v1_0_prefix = '/api/v1.0'

app.register_blueprint(light_mod, url_prefix=v1_0_prefix)
