from typing import Dict

import os
import sdm_modbus


class PhaseMeter:
    def __init__(self):
        self.device = sdm_modbus.SDM120(device="/dev/ttyUSB0",
                                        unit=1,
                                        baud=9600,
                                        parity="N")

        # self.device = sdm_modbus.SDM120(device=os.getenv("COM_PORT"),
        #                                 unit=int(os.getenv("MODBUS_ADDRESS")),
        #                                 baud=int(os.getenv("BAUD_RATE")),
        #                                 parity=os.getenv("PARITY"))

    def get_measurement(self) -> Dict:
        if not self.device.connected():
            return {"status": "not connected"}
        results = self.device.read_all(1)
        print(results)
        return results
        # return self.device.read_all(1) # sdm_modbus.registerType.INPUT
