from app.models.device import Device


# get
async def get_devices_service() -> list[Device]:
    pass


# get single device
async def get_device_service(device_id: int) -> Device:
    pass


# post create device
async def create_device_service(payload) -> Device:
    pass


# patch
async def update_device_service(device_id: int, payload) -> Device:
    pass


# delete
async def delete_device_service(device_id: int):
    pass
