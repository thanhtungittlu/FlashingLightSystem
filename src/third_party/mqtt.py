import paho.mqtt.client as mqtt
import ssl
import pymongo
from src.models.mongo.state_messages import StateMessaghes
from configs import MQTTConfig


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTTConfig.TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    StateMessaghes().insert({"topic": msg.topic, "payload": msg.payload})

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(ca_certs=MQTTConfig.ROOTCA, certfile=MQTTConfig.CERTIFICATE, keyfile=MQTTConfig.PRIVATE_KEY, tls_version=ssl.PROTOCOL_TLSv1_2)

client.connect(MQTTConfig.HOST, MQTTConfig.PORT, 60)
client.loop_forever()
