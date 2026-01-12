from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.db.session import get_db

router = APIRouter(prefix="/health", tags=["health"])


# api health check
@router.get("/")
async def health_check():
    return {"status": "ok"}


# db health check
@router.get("/db")
async def db_health_check(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"database": "ok"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable",
        )
