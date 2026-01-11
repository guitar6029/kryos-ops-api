from fastapi import APIRouter, status, HTTPException
from app.schemas.operator import OperatorCreate, OperatorResponse

## tags are used for swapper api, helps routes keep rganzied 
router = APIRouter(prefix="/operators", tags=["operators"])


@router.post("", response_model=OperatorResponse, status_code=status.HTTP_201_CREATED)
async def create_operator(payload: OperatorCreate):
    # if error
    if payload.codename.lower() == "admin":
        raise HTTPException(status_code=400, detail="Invalid codename")

    # if good
    return {
        "id": 1,
        "codename": payload.codename,
        "clearance": payload.clearance,
        "active": payload.active,
    }
