from pydantic import BaseModel, Field
from typing import Optional
from app.enums.device_status import DeviceStatus
from app.enums.device_kind import DeviceKind

# for post
class DeviceCreate(BaseModel):
    kind: DeviceKind
    status: DeviceStatus = DeviceStatus.OFFLINE
    battery: int = Field(default=100, ge=1, le=100)


# for the get response
class DeviceResponse(BaseModel):
    kind: DeviceKind
    status: DeviceStatus
    battery: int = Field(ge=1, le=100)


#for update
class DeviceUpdate(BaseModel):
    kind: Optional[DeviceKind]
    status: Optional[DeviceStatus]
    battery: Optional[int] = Field(ge=1, le=100)