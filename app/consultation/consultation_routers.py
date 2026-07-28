from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.auth.auth_dependencies import get_staff_or_admin

from . import consultation_crud

from .consultation_schemas import (
    ConsultationCreate,
    ConsultationUpdate,
    ConsultationResponse
)

router = APIRouter(
    prefix="/consultations",
    tags=["Consultations"]
)

# ==========================================
# CREATE
# ADMIN + STAFF
# ==========================================

@router.post("/", response_model=ConsultationResponse)
def create_consultation(
    data: ConsultationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    return consultation_crud.create_consultation(
        db,
        data
    )


# ==========================================
# READ ALL
# ADMIN + STAFF
# ==========================================

@router.get("/", response_model=list[ConsultationResponse])
def read_consultations(
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    return consultation_crud.get_all_consultations(db)


# ==========================================
# READ ONE
# ADMIN + STAFF
# ==========================================

@router.get("/{id}", response_model=ConsultationResponse)
def read_one(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    consultation = consultation_crud.get_consultation_by_id(
        db,
        id
    )

    if not consultation:

        raise HTTPException(
            status_code=404,
            detail="Consultation not found"
        )

    return consultation


# ==========================================
# UPDATE
# ADMIN + STAFF
# ==========================================

@router.put("/{id}", response_model=ConsultationResponse)
def update(
    id: int,
    data: ConsultationUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    consultation = consultation_crud.update_consultation(
        db,
        id,
        data
    )

    if not consultation:

        raise HTTPException(
            status_code=404,
            detail="Consultation not found"
        )

    return consultation


# ==========================================
# DELETE
# ADMIN + STAFF
# ==========================================

@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    consultation = consultation_crud.delete_consultation(
        db,
        id
    )

    if not consultation:

        raise HTTPException(
            status_code=404,
            detail="Consultation not found"
        )

    return {

        "message": "Consultation deleted successfully"

    }