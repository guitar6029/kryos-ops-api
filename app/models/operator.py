from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Enum as SQLEnum
from app.db.base import Base
from app.db.types.operator_role import OperatorRole


class Operator(Base):
    __tablename__ = "operators"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    full_name = Column(String(120), nullable=False)
    role = Column(SQLEnum(OperatorRole), nullable=False, server_default="operator")
    is_active = Column(Boolean, nullable=False, server_default="true")

    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
