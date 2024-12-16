from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    restaurant_id: int | None


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime


class UserPatch(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    restaurant_id: Optional[int] = None

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    password_confirmation: str

class UserFormToken(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str