from pydantic import BaseModel

class PermissionBase(BaseModel):
    name: str
    description: str
    role_id: int

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True
