from pydantic import BaseModel


# ==========================================
# Login Request
# ==========================================

class LoginRequest(BaseModel):

    username: str

    password: str


# ==========================================
# Login Response
# ==========================================

class LoginResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"


# ==========================================
# Current User
# ==========================================

class CurrentUser(BaseModel):

    user_id: int

    username: str

    role: str

    staff_id: int

    is_active: bool