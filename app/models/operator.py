from sqlalchemy import Column, Integer
from app.db.base import Base

class Operator(Base):
    __tablename__ = "operators"
    id = Column(Integer, primary_key=True)