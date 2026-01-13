from pydantic import BaseModel, Field
from app.enums.device_status import DeviceStatus
from app.enums.device_kind import DeviceKind


class DeviceCreate(BaseModel):
    kind: DeviceKind
    status: DeviceStatus = DeviceStatus.OFFLINE
    battery: int = Field(default=100, ge=1, le=100)


class DeviceResponse(BaseModel):
    kind: DeviceKind
    status: DeviceStatus
    battery: int = Field(ge=1, le=100)
