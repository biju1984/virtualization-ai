
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models.database import Base

role_permissions = Table(
    'role_permissions',
    Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey(
        'permissions.id'), primary_key=True)
)
