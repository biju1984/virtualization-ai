from pydantic import BaseModel, EmailStr, Field, FieldValidationInfo, field_validator
from typing import Optional


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


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
