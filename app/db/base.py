from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Operator(Base):
    __tablename__ = "operators"
    id = Column(Integer, primary_key=True)
