from sqlalchemy import Column, Integer, String, JSON, DateTime, func, Index
from sqlalchemy.dialects.postgresql import JSONB
from app.models.database import Base


class Specification(Base):
    __tablename__ = "specifications"

    id = Column(Integer, primary_key=True, index=True)
    version = Column(Integer, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    spec_type = Column(String, nullable=False)  # JSON or YAML
    spec = Column(JSONB, nullable=False)  # Store JSON data directly
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (Index('ix_spec_jsonb', 'spec', postgresql_using='gin'),)
