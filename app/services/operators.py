from app.schemas.operator import OperatorCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.operator import Operator


async def create_operator_service(
    db: AsyncSession, payload: OperatorCreate
) -> Operator:
    operator = Operator(**payload.model_dump())
    # add operator
    db.add(operator)
    await db.commit()
    await db.refresh(operator)
    return operator
