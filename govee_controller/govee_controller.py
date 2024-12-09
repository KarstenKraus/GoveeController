from typing import Optional
from govee_logger import GoveeLogger, LogTypes
from govee_device import Device
import requests
import sys
import json

BASE_HOST = "https://openapi.api.govee.com/"

LOGGER = GoveeLogger()

class GoveeController:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Govee-API-Key": api_key
        }

    def GetDevices(self) -> list[Device]:
        devices = []
        r = requests.get(BASE_HOST + "router/api/v1/user/devices", headers=self.headers)

        if r.status_code == 429:
            LOGGER.Log(LogTypes.ERROR, "Daily rate limit reached!")
            sys.exit(1)

        if r.status_code == 401:
            LOGGER.Log(LogTypes.ERROR, "Invalid API key provided!")
            sys.exit(1)

        data = json.loads(r.text)
        deviceCount = len(data)

        for i in range(deviceCount):
            devices.append(Device(data["data"][i]["sku"], data["data"][i]["device"]))

        return devices
    
    def GetDeviceState(self, device: Device):
        r = requests.get(BASE_HOST + "router/api/v1/device/state", headers=self.headers, data=device.GeneratePayload())
        if r.status_code == 429:
            LOGGER.Log(LogTypes.ERROR, "Daily rate limit reached!")
            sys.exit(1)

        if r.status_code == 401:
            LOGGER.Log(LogTypes.ERROR, "Invalid API key!")
            sys.exit(1)

        return json.loads(r.text)