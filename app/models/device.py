from sqlalchemy import Column, Integer, func, DateTime, Enum as SQLEnum
from app.db.base import Base
from app.enums.device_kind import DeviceKind
from app.enums.device_status import DeviceStatus


# default is applied by SQLAlchemy (Python-side).
# server_default is applied by the database itself.


class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    kind = Column(SQLEnum(DeviceKind, name="device_kind"), nullable=False)
    status = Column(
        SQLEnum(DeviceStatus, name="device_status"),
        nullable=False,
        server_default="OFFLINE",
    )
    battery = Column(Integer, nullable=False, server_default="100")
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
