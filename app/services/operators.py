from app.schemas.operator import OperatorCreate, OperatorResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.operator import Operator


async def create_operator(db: AsyncSession, payload: Operator) -> OperatorResponse:
    operator = Operator(**payload.model_dump())
    # add operator
    db.add(operator)
    await db.commit()
    await db.refresh(operator)
    return operator
