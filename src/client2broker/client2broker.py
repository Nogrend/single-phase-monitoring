import os
import uuid
from datetime import datetime
from enum import Enum
from typing import Dict

import paho.mqtt.client as mqtt
from json import dumps


class Client2Broker:
    class AllowedTopics(Enum):
        STATUS = "status"
        MEASUREMENT_ALL = "measurement/all"
        TOTAL_ENERGY_ACTIVE = "measurement/totalEnergyActive"

    def __init__(self):
        self.topic_base = os.getenv("MQTT_TOPIC")

        self.client = mqtt.Client()
        self.client.username_pw_set(username=os.getenv("MQTT_USERNAME"),
                                    password=os.getenv("MQTT_PASSWORD"))

        self.client.on_connect = self.on_connect

        self.client.connect(os.getenv("MQTT_BROKER_ADDRESS"),
                            int(os.getenv("MQTT_PORT")),
                            60)

    @staticmethod
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT Broker with result code " + str(rc))

    @staticmethod
    def build_payload_with_id_and_timestamp(content: Dict) -> Dict:
        payload: Dict = content
        payload["id"] = str(uuid.uuid4())
        payload["timestamp"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return payload

    def sent_to_broker(self, payload, topic: AllowedTopics) -> None:
        measurement_dump: str = dumps(payload)
        topic = self.topic_base + topic
        self.client.publish(topic=topic,
                            payload=measurement_dump)
