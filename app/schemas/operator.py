from pydantic import BaseModel, Field


class OperatorCreate(BaseModel):
    codename: str = Field(min_length=2, max_length=32)
    clearance_level: int = Field(ge=1, le=5)
    active: bool = True
