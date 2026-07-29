from typing import Optional
from pydantic import BaseModel, ConfigDict


# ==========================
# Base Schema
# ==========================

class UserBase(BaseModel):

    username: str
    role: str
    is_active: bool
    staff_id: Optional[int] = None


# ==========================
# Create User
# ==========================

class UserCreate(BaseModel):

    username: str
    password: str
    role: str
    staff_id: Optional[int] = None


# ==========================
# Update User
# ==========================

class UserUpdate(BaseModel):

    username: str
    role: str
    is_active: bool


# ==========================
# Read User
# ==========================

class User(UserBase):

    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )