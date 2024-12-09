from enum import Enum

class LogTypes(Enum):
    INFO = 1,
    WARNING = 2,
    ERROR = 3,
    DEBUG = 4

LOG_COLORS = {
    LogTypes.INFO: "[32m",
    LogTypes.WARNING: "[33m",
    LogTypes.ERROR: "[31m",
    LogTypes.DEBUG: "[36m"
}

class GoveeLogger:
    def __init__(self):
        pass

    def Log(self, logType, message):
        color = LOG_COLORS[logType]
        print("\033" + color + message + "\033[0m")