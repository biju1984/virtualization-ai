from sqlalchemy import Column, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base

class Version(Base):
    __tablename__ = 'versions'
    id = Column(Integer, primary_key=True, index=True)
    api_specification_id = Column(Integer, ForeignKey('api_specifications.id'))
    version_number = Column(Integer)
    request_structure = Column(JSON)
    response_structure = Column(JSON)
    api_specification = relationship("APISpecification", back_populates="versions")
