from fastapi import APIRouter, status, HTTPException, Depends
from app.schemas.operator import OperatorCreate, OperatorResponse
from app.services.operators import create_operator_service
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db

## tags are used for swapper api, helps routes keep rganzied
router = APIRouter(prefix="/operators", tags=["operators"])


@router.post("", response_model=OperatorResponse, status_code=status.HTTP_201_CREATED)
async def create_operator(
    payload: OperatorCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await create_operator_service(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
