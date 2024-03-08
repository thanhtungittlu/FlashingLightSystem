from src.models.mongo.lights import LightStructure,Lights
from src.common.utils import to_dict

class LightsControlller():
    def ping(self):
        return  {
            "code": 200,
            "data": [],
            "message": "success"
        }
    
