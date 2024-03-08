from src.models.mongo.lights import LightStructure,Lights
from src.common.utils import to_dict, validate_uuid

class LightsControlller():
    def ping(self):
        return  {
            "code": 200,
            "data": [],
            "message": "success"
        }
    

    def sort_light_by_color(self, list_light):
        color_order = {
            "red": 0,
            "orange": 1,
            "yellow": 2,
            "green": 3,
            "blue": 4,
            "indigo": 5,
            "violet": 6
        }
        return sorted(list_light, key=lambda x: color_order.get(x["light_color"], float('inf')))

    def list_light_in_room(self, room_id):
        if not validate_uuid(room_id):
            return {
                "code": 400,
                "message": "error",
                "reason": "UUID is valid"
            }
        lights_model = Lights()
        lights = lights_model.collector().find({'room_id': room_id})
        res = self.sort_light_by_color(to_dict(lights))
        return  {
            "code": 200,
            "data": res,
            "message": "success"
        }