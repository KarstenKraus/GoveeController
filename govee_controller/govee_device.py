class Device:
    def __init__(self, sku, device):
        self.sku = sku
        self.device = device

    def GetSKU(self) -> str:
        return self.sku
    
    def GetDeviceID(self) -> str:
        return self.device