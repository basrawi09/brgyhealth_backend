from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.auth.auth_dependencies import (
    get_admin_user,
    get_staff_or_admin
)

from . import staff_crud

from .staff_schemas import (
    StaffCreate,
    StaffUpdate,
    StaffResponse
)

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)

# ==========================================
# CREATE STAFF (ADMIN ONLY)
# ==========================================

@router.post(
    "/",
    response_model=StaffResponse
)
def create_staff(
    staff: StaffCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    return staff_crud.create_staff(
        db,
        staff
    )


# ==========================================
# READ ALL STAFF
# ADMIN + STAFF
# ==========================================

@router.get("/")
def get_staff(

    db: Session = Depends(get_db),

    current_user=Depends(get_staff_or_admin)

):

    return staff_crud.get_all_staff(db)


# ==========================================
# READ ONE STAFF
# ADMIN + STAFF
# ==========================================

@router.get(
    "/{staff_id}",
    response_model=StaffResponse
)
def read_one(

    staff_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_staff_or_admin)

):

    staff = staff_crud.get_staff_by_id(
        db,
        staff_id
    )

    if not staff:

        raise HTTPException(
            404,
            "Staff not found"
        )

    return staff


# ==========================================
# UPDATE STAFF
# ADMIN ONLY
# ==========================================

@router.put(
    "/{staff_id}",
    response_model=StaffResponse
)
def update(

    staff_id: int,

    data: StaffUpdate,

    db: Session = Depends(get_db),

    current_user=Depends(get_admin_user)

):

    staff = staff_crud.update_staff(
        db,
        staff_id,
        data
    )

    if not staff:

        raise HTTPException(
            404,
            "Staff not found"
        )

    return staff


# ==========================================
# DELETE STAFF
# ADMIN ONLY
# ==========================================

@router.delete("/{staff_id}")
def delete(

    staff_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(get_admin_user)

):

    staff = staff_crud.delete_staff(
        db,
        staff_id
    )

    if not staff:

        raise HTTPException(
            404,
            "Staff not found"
        )

    return {

        "message": "Staff deleted successfully"

    }