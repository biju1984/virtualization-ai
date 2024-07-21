from sqlalchemy import Column, Integer, String, Text
from app.models.database import Base

class Specification(Base):
    __tablename__ = "specifications"

    id = Column(Integer, primary_key=True, index=True)
    version = Column(Integer, index=True)
    spec = Column(Text, nullable=False)
