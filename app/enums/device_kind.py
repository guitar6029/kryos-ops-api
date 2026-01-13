from enum import Enum


class DeviceKind(str, Enum):
    DRONE = "DRONE"
    EXO = "EXO"
    SENSOR = "SENSOR"
