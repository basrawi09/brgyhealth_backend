from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.auth.auth_dependencies import get_admin_user

from . import user_crud

from .user_schemas import (
    User,
    UserCreate,
    UserUpdate
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# ==========================================
# Get All Users
# ==========================================

@router.get(
    "/",
    response_model=list[User]
)
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    return user_crud.get_users(db)


# ==========================================
# Get User by ID
# ==========================================

@router.get(
    "/{user_id}",
    response_model=User
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    user = user_crud.get_user(
        db,
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return user


# ==========================================
# Create User
# ==========================================

@router.post(
    "/",
    response_model=User,
    status_code=201
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    return user_crud.create_user(
        db,
        user
    )


# ==========================================
# Update User
# ==========================================

@router.put(
    "/{user_id}",
    response_model=User
)
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    user = user_crud.update_user(
        db,
        user_id,
        updated_user
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return user

# ==========================================
# Toggle User Status
# ==========================================

@router.patch(
    "/{user_id}/toggle",
    response_model=User
)
def toggle_status(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    user = user_crud.toggle_user_status(
        db,
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return user

# ==========================================
# Delete User
# ==========================================

@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    user = user_crud.delete_user(
        db,
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    return {

        "message": "User deleted successfully."

    }