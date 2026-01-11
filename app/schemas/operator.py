from pydantic import BaseModel, Field
from app.types import Clearance


class OperatorCreate(BaseModel):
    codename: str = Field(min_length=2, max_length=32)
    clearance: Clearance
    active: bool = True


class OperatorResponse(BaseModel):
    id: int = Field(
        ge=1,
    )
    codename: str = Field(min_length=2)
    clearance: Clearance
    active: bool
