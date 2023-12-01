from sqlalchemy import Column, Integer, String
from .database import Base

class MonModel(Base):
    __tablename__ = "ma_table"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    description = Column(String, index=True)
