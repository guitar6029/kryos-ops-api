from sqlalchemy import Column, Integer
from app.db.base import Base

class Operator(Base):
    __table__ = "operators"
    id = Column(Integer, primary_key=True)