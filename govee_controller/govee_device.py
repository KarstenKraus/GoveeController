import json

class Device:
    def __init__(self, sku, device):
        self.sku = sku
        self.device = device

    def GetSKU(self) -> str:
        return self.sku
    
    def GetDeviceID(self) -> str:
        return self.device
    
    def GeneratePayload(self) -> str: # JSON payload for use in the cursed API
        data = {
            "requestId": "uuid", # Wtf is this?
            "payload": {
                "sku": self.sku,
                "device": self.device
            }
        }
        return json.dumps(data)
