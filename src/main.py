#!/usr/bin/env python3

from dotenv import load_dotenv
from phase_meter import PhaseMeter
from client2broker import Client2Broker

load_dotenv()

if __name__ == "__main__":
    phase_meter = PhaseMeter()
    client_2_broker = Client2Broker()

    client_2_broker.sent_to_broker({"status": "running"})

    is_running: bool = True
    while is_running:
        measurement = phase_meter.get_measurement()
        client_2_broker.sent_to_broker(measurement)

        is_running = False
        print("stop")
        client_2_broker.sent_to_broker({"status": "dead"})

## !/usr/bin/env python3

# import os
# from dotenv import load_dotenv
#
#
# import sdm_modbus
# import paho.mqtt.client as mqtt
#
# if __name__ == "__main__":
#
#     load_dotenv()
#
#     # Parameters for communication through USB
#     # com_port = "/dev/tty.usbserial-00000000"
#     com_port = os.getenv("COM_PORT")
#     modbus_address = 1  # Replace with the correct Modbus address
#     baud_rate = 9600  # Replace with the correct baud rate
#     parity = "N"
#
#     # MQTT Broker Settings
#     mqtt_broker_address: str = os.getenv("MQTT_BROKER_ADDRESS")
#     mqtt_topic: str = os.getenv("MQTT_TOPIC")
#     mqtt_port: int = int(os.getenv("MQTT_PORT"))
#     mqtt_username: str = os.getenv("MQTT_USERNAME")
#     mqtt_password: str = os.getenv("MQTT_PASSWORD")
#
#     # Create an MQTT client instance
#     client = mqtt.Client()
#
#
#     # Callback when the client connects to the MQTT broker
#     def on_connect(client, userdata, flags, rc):
#         print("Connected to MQTT Broker with result code " + str(rc))
#
#
#     # Set the username and password for the MQTT broker
#     client.username_pw_set(username=mqtt_username, password=mqtt_password)
#
#     # Connect to the MQTT broker
#     client.on_connect = on_connect
#     client.connect(mqtt_broker_address, mqtt_port, 60)
#
#     device = sdm_modbus.SDM120(device=com_port, unit=modbus_address, baud=baud_rate, parity=parity)
#
#     # try:
#     device_measurement = device.read_all(sdm_modbus.registerType.INPUT)
#     for key, value in device_measurement.items():
#         print(key, value)
#
#     # Convert the device_measurement dictionary to a JSON string
#     import json
#
#     measurement_json = json.dumps(device_measurement)
#
#     # Publish the measurement to the MQTT topic
#     client.publish(mqtt_topic, measurement_json)
#
#     # except KeyboardInterrupt:
#     #     print("Program stopped by user.")
#
#     # Keep the MQTT client running to ensure the message is published
#     # client.loop_forever()
