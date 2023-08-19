import paho.mqtt.publish as publish
import sdm_modbus
from json import dumps

from secrets import *

# Replace these parameters with appropriate values
com_port = "COM7"
modbus_address = 1  # Replace with the correct Modbus address
baud_rate = 9600  # Replace with the correct baud rate
parity = "N"

device = sdm_modbus.SDM120(device=com_port, unit=modbus_address, baud=baud_rate, parity=parity)
print(device.connected())

# Continuously read and print the voltage value
device_measurement: dict={}
try:
    device_measurement = device.read_all(sdm_modbus.registerType.INPUT)
    for key, value in device_measurement.items():
        print(key, value)
except KeyboardInterrupt:
    print("Program stopped by user.")

datadump:str= dumps(device_measurement)

publish.single(topic=MQTT_PATH, payload=datadump, hostname=MQTT_SERVER, auth=auth)
