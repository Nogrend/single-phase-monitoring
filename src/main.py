from phase_meter import PhaseMeter

from dotenv import load_dotenv

from client2broker import Client2Broker

load_dotenv()


if __name__ == "__main__":
    phase_meter = PhaseMeter()
    client_2_broker = Client2Broker()

    client_2_broker.sent_to_broker({"status": "running"})

    is_running: bool = True
    while is_running:
        measurement = phase_meter.get_measurement()
        measurement = {"voltage": 230}
        client_2_broker.sent_to_broker(measurement)

        is_running = False
        print("stop")

