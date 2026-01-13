from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.device import DeviceCreate, DeviceResponse, DeviceUpdate
from app.services.devices import (
    create_device_service,
    delete_device_service,
    get_device_service,
    get_devices_service,
    update_device_service,
)

router = APIRouter(prefix="/devices", tags=["devices"])


# GET , get list of devices
@router.get("/", response_model=list[DeviceResponse])
async def get_devices(db: AsyncSession = Depends(get_db)):
    try:
        return await get_devices_service(db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# get device
@router.get("/{device_id}", response_model=DeviceResponse)
async def get_device(device_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await get_device_service(db, device_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# POST, create a device
@router.post("/", response_model=DeviceResponse, status_code=status.HTTP_201_CREATED)
async def create_device(payload: DeviceCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_device_service(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# PATCH update a device , based on id
@router.patch("/{device_id}", response_model=DeviceResponse)
async def update_device(
    device_id: int, payload: DeviceUpdate, db: AsyncSession = Depends(get_db)
):
    try:
        return await update_device_service(db, device_id, payload)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# DELETE , delete a device, based on id
@router.delete("/{device_id}")
async def delete_device(device_id: int, db: AsyncSession = Depends(get_db)):
    try:
        await delete_device_service(db, device_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
