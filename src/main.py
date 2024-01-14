from time import sleep
from dotenv import load_dotenv

from phase_meter import PhaseMeter
from client2broker import Client2Broker

load_dotenv()

if __name__ == "__main__":
    phase_meter = PhaseMeter()
    mqtt = Client2Broker()

    payload = mqtt.build_payload_with_id_and_timestamp({"message": "starting script"})
    mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.STATUS)

    is_running: bool = True
    while is_running:
        measurement = phase_meter.get_measurement()

        if measurement == {}:
            content = ""
            payload = mqtt.build_payload_with_id_and_timestamp({"message": "no data received"})
            mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.STATUS)

        else:
            payload = mqtt.build_payload_with_id_and_timestamp(measurement)
            mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.MEASUREMENT_ALL)

        sleep(60)

    payload = mqtt.build_payload_with_id_and_timestamp({"message": "script down"})
    mqtt.sent_to_broker(payload, Client2Broker.AllowedTopics.STATUS)
