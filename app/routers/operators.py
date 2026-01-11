from fastapi import APIRouter
from app.schemas.operator import OperatorCreate, OperatorResponse

router = APIRouter(prefix="/operators", tags=["operators"])

@router.post("", response_model=OperatorResponse)
async def create_operator(payload: OperatorCreate):
    return {
        "id": 1,
        "codename": payload.codename,
        "clearance": payload.clearance,
        "active": payload.active
    }