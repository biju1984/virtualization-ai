from pydantic import BaseModel, EmailStr, Field, FieldValidationInfo, field_validator
from typing import Optional
from app.models.role import Role


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None  # Optional full_name field


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)

    @field_validator('password')
    def validate_password(cls, v: str, info: FieldValidationInfo) -> str:
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isalpha() for char in v):
            raise ValueError('Password must contain at least one letter')
        return v


class RoleResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class UserResponse(UserBase):
    id: int
    is_active: bool
    role: Optional[RoleResponse]  # Use RoleResponse schema

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    token: str
    version: str
    message: str


class User(BaseModel):  # New User schema
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool
    role_id: Optional[int] = None

    class Config:
        orm_mode = True
