from govee_controller import GoveeController
from govee_logger import GoveeLogger, LogTypes

def read_key_config():
    with open("api_key.txt", "r") as f:
        return f.read()

API_KEY = read_key_config()
CONTROLLER = GoveeController(API_KEY)
DEVICES = CONTROLLER.GetDevices()