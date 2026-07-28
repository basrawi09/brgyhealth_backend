from pydantic import BaseModel, ConfigDict


# ==========================
# Base Schema
# ==========================

class UserBase(BaseModel):

    username: str
    role: str
    is_active: bool
    staff_id: int


# ==========================
# Create User
# ==========================

class UserCreate(BaseModel):

    username: str
    password: str
    role: str
    staff_id: int


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