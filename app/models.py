from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MonModel(Base):
    __tablename__ = "ma_table"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    description = Column(String, index=True)
