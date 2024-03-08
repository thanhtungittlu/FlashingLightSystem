from src.models.mongo.base_model import BaseModel
from src.common import ClassEnumBase


class LightStructure(ClassEnumBase):
    _ID = '_id'
    LIGHT_ID = 'light_id'
    ROOM_ID = 'room_id'
    LIGHT_NAME = 'light_name'
    LIGHT_FLASHING_CYCLE_TIME = 'light_flashing_cycle_time'



class Lights(BaseModel):
    collection_name = 'lights'
