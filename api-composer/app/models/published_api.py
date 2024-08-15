from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.database import Base

class PublishedAPI(Base):
    __tablename__ = 'published_apis'
    id = Column(Integer, primary_key=True, index=True)
    api_specification_id = Column(Integer, ForeignKey('api_specifications.id'))
    version_id = Column(Integer, ForeignKey('versions.id'))
    url = Column(String, unique=True)
