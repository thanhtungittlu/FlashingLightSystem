from src.models.mongo.lights import LightStructure,Lights
from src.common.utils import to_dict

class LightsControlller():
    def ping(self):
        data = Lights().collector().find({})
        return  {
            "code": 200,
            "data": to_dict(data),
            "message": "success"
        }
    
