from src.apis.v1_0 import *
from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)