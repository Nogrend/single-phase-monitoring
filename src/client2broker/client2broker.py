import os

import paho.mqtt.client as mqtt
from json import dumps


class Client2Broker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(username=os.getenv("MQTT_USERNAME"),
                                    password=os.getenv("MQTT_PASSWORD"))

        self.client.on_connect = self.on_connect

        self.client.connect(os.getenv("MQTT_BROKER_ADDRESS"),
                            int(os.getenv("MQTT_PORT")),
                            60)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT Broker with result code " + str(rc))

    def sent_to_broker(self, measurement) -> None:
        measurement_dump: str = dumps(measurement)
        self.client.publish(topic=os.getenv("MQTT_TOPIC"),
                            payload=measurement_dump)
