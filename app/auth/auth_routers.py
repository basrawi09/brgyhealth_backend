from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from . import auth_crud

from .auth_schemas import (
    LoginRequest,
    LoginResponse,
    CurrentUser
)

from .auth_dependencies import get_current_user

from app.user.user_models import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==========================================
# Login
# ==========================================

@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    result = auth_crud.login_user(
        db,
        request.username,
        request.password
    )

    if result is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password."
        )

    return result


# ==========================================
# Current Logged-in User
# ==========================================

@router.get(
    "/me",
    response_model=CurrentUser
)
def get_me(
    current_user: User = Depends(get_current_user)
):

    return {

        "user_id": current_user.user_id,

        "username": current_user.username,

        "role": current_user.role,

        "staff_id": current_user.staff_id,

        "is_active": current_user.is_active

    }