# FlashingLightSystem
This project aims to develop an API that allows users to retrieve the schedule setting of the flashing light system.

This version returns an API that lists the light bulbs in a room along with the interval between two nearest switch-ons.
API (GET): {host}/api/v1.0/light/lights-in-room/<room_id>

# Run App
Step1: change Env\\
Step2: Create index: python ensure_indexes_mongo.py\\
Step3: Install lib in enviroment: pip install -r requirements.txt\\
step4: Run app: python app.py\\

# Enviroment
| Env name | Example vallue | Description |
|---------|---------|-----------------|
| APP_NAME  |  Flasing Light System    | App Name      |
| WORKING_DIR   | /home/tunglt/Dev/FlashingLightSystem    | Working dir  |
| MONGO_URI   |  abcd  | config mqtt  |
| MQTT_HOST   | abcd    | config mqtt    |
| MQTT_PORT   | abcd    | config mqtt    |
| MQTT_CERTIFICATE   | abcd    | config mqtt    |
| MQTT_PRIVATE_KEY   | abcd    | config mqtt    |
| MQTT_ROOTCA   | abcd    | config mqtt    |
| MQTT_TOPIC   | abcd    | config mqtt    |
