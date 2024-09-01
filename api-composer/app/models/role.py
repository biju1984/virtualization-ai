from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.database import Base
# Import the association table
from app.models.role_permission import role_permissions


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

    # Relationship with users
    users = relationship("User", back_populates="role")

    # Many-to-many relationship with permissions
    permissions = relationship(
        "Permission", secondary=role_permissions, back_populates="roles")
