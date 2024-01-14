from time import sleep
from typing import List

from dotenv import load_dotenv

from phase_meter import PhaseMeter
from client2broker import Client2Broker

load_dotenv()

if __name__ == "__main__":
    phase_meter = PhaseMeter()
    mqtt = Client2Broker()

    content = {"message": "starting script"}
    payload = mqtt.build_payload_with_id_and_timestamp(content)
    mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.STATUS)

    is_running: bool = True
    quantities: List = ["power_active", "total_energy_active"]
    while is_running:
        measurement = phase_meter.get_measurement_with_quantities(quantities)

        if measurement == {}:
            content = {"message": "no data received"}
            payload = mqtt.build_payload_with_id_and_timestamp(content)
            mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.STATUS)

        else:
            payload = mqtt.build_payload_with_id_and_timestamp(measurement)
            mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.MEASUREMENT_ALL)

        sleep(60)

    content = {"message": "script down"}
    payload = mqtt.build_payload_with_id_and_timestamp(content)
    mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.STATUS)
