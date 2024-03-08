import os
from pymongo import MongoClient

class ApplicationConfig():
    NAME = str(os.environ.get("APP_NAME"))
    WORKING_DIR = str(os.environ.get("WORKING_DIR"))

class MongoConfig:
    uri = os.environ.get('MONGO_URI')
    db_name = 'light_db'

def mongodb_init():
    global global_company_mongodb_client
    if global_company_mongodb_client is None:
        global_company_mongodb_client = MongoClient(MongoConfig.uri)
    return global_company_mongodb_client

class MQTTConfig:
    HOST = os.environ.get("MQTT_HOST")
    PORT = os.environ.get("MQTT_PORT")
    CERTIFICATE = os.environ.get("MQTT_CERTIFICATE")
    PRIVATE_KEY = os.environ.get("MQTT_PRIVATE_KEY")
    ROOTCA = os.environ.get("MQTT_ROOTCA")
    TOPIC = os.environ.get("MQTT_TOPIC")
    
    
