
#get 
async def get_devices_service() -> list[DeviceResponse]:
    pass

#get single device
async def get_device_service(device_id: int) -> DeviceResponse:
    pass
#post create device
async def create_device_service(payload) -> DeviceResponse:
    pass

#patch
async def update_device_service(device_id:  int, payload) -> DeviceResponse:
    pass 

#delete
async def delete_device_service(device_id: int):
    pass