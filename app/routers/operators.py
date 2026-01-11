from fastapi import APIRouter, status, HTTPException
from app.schemas.operator import OperatorCreate, OperatorResponse
from app.services.operators import create_operator as create_ops_service

## tags are used for swapper api, helps routes keep rganzied
router = APIRouter(prefix="/operators", tags=["operators"])


@router.post("", response_model=OperatorResponse, status_code=status.HTTP_201_CREATED)
async def create_operator(payload: OperatorCreate):
    try:
        return await create_ops_service(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
