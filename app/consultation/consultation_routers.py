from datetime import date

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
# ==========================================

@router.get("/", response_model=list[ConsultationResponse])
def read_consultations(
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    return consultation_crud.get_all_consultations(db)


# ==========================================
# CALENDAR SCHEDULE
# ==========================================

@router.get("/calendar/")
def calendar_schedule(
    date_selected: date,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    consultations = consultation_crud.get_calendar_schedule(
        db,
        date_selected
    )

    return [

        {
            "consultation_id": c.consultation_id,
            "patient_id": c.patient.patient_id,
            "patient_name": f"{c.patient.firstname} {c.patient.lastname}",
            "consultation_date": c.consultation_date,
            "consultation_time": c.consultation_time,
            "diagnosis": c.diagnosis,
            "medicine": c.medicine
        }

        for c in consultations

    ]


# ==========================================
# READ ONE
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