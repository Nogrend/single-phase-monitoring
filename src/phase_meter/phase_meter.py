from typing import Dict, List

import os
import sdm_modbus


class PhaseMeter:
    def __init__(self):
        self.device = sdm_modbus.SDM120(device=os.getenv("COM_PORT"),
                                        unit=int(os.getenv("MODBUS_ADDRESS")),
                                        baud=int(os.getenv("BAUD_RATE")),
                                        parity=os.getenv("PARITY"))

    def get_all_measurements(self) -> Dict:
        if not self.device.connected():
            return {}
        return self.device.read_all(sdm_modbus.registerType.INPUT)

    def get_measurement_with_quantities(self, quantities: List[str]) -> Dict:
        if not self.device.connected():
            return {}

        measurements: Dict = {}

        for quantity in quantities:
            measurements[quantity] = round(self.device.read(quantity), 2)

        return measurements
