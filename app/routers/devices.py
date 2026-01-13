from fastapi import APIRouter, status, HTTPException

from app.schemas.device import DeviceCreate, DeviceResponse

# TODO
# schemas
# and services

router = APIRouter(prefix="/devices", tags=["devices"])


# GET , get list of devices
@router.get("/", response_model=list[DeviceResponse])
async def get_devices():
    try:
        return await get_devices_service()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# POST, create a device
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_device(payload: DeviceCreate):
    try:
        return await create_device_service(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# PATCH update a device , based on id
@router.patch("/{device_id}")
async def update_device(device_id: str, payload: DeviceUpdate):
    try:
        return await update_device_service(device_id, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# DELETE , delete a device, based on id
@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_device(device_id: str):
    try:
        return await delete_device_service(device_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
