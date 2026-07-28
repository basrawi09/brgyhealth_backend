from sqlalchemy.orm import Session

from app.user.user_models import User

from .auth_security import (
    verify_password,
    create_access_token
)


# ==========================================
# Authenticate User
# ==========================================

def authenticate_user(
    db: Session,
    username: str,
    password: str
):

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if not user:

        return None

    if not user.is_active:

        return None

    if not verify_password(
        password,
        user.password_hash
    ):

        return None

    return user


# ==========================================
# Login
# ==========================================

def login_user(
    db: Session,
    username: str,
    password: str
):

    user = authenticate_user(
        db,
        username,
        password
    )

    if not user:

        return None

    token = create_access_token(

        {
            "sub": user.username,
            "user_id": user.user_id,
            "role": user.role,
            "staff_id": user.staff_id
        }

    )

    return {

        "access_token": token,

        "token_type": "bearer"

    }