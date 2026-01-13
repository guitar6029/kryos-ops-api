from app.models.device import Device
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas.device import DeviceCreate, DeviceUpdate


# get
async def get_devices_service(db: AsyncSession) -> list[Device]:
    stmt = select(Device)
    result = await db.execute(stmt)
    devices = result.scalars().all()
    return devices


# get single device
async def get_device_service(db: AsyncSession, device_id: int) -> Device:
    stmt = select(Device).where(Device.id == device_id)
    result = await db.execute(stmt)
    device = result.scalar_one_or_none()
    if device is None:
        raise ValueError("Device not found")
    return device


# post create device
async def create_device_service(db: AsyncSession, payload: DeviceCreate) -> Device:
    device = Device(**payload.model_dump())
    db.add(device)
    await db.commit()
    await db.refresh(device)
    return device


# patch
async def update_device_service(
    db: AsyncSession, device_id: int, payload: DeviceUpdate
) -> Device:
    # first find the device in the table
    device = await get_device_service(db, device_id)
    ## if result exists
    data = payload.model_dump(exclude_unset=True)

    # no patch
    if not data:
        return device

    # continue if not { }
    for key, value in data.items():
        setattr(device, key, value)

    ## update the row
    await db.commit()

    # refresh to get updated db state
    await db.refresh(device)

    return device


# delete
async def delete_device_service(db: AsyncSession, device_id: int) -> None:
    # check if exists
    device = await get_device_service(db, device_id)
    # delete row
    await db.delete(device)
    await db.commit()

    return None
