from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.auth.auth_dependencies import (
    get_admin_user,
    get_staff_or_admin
)

from . import patient_crud

from .patient_schemas import (
    PatientCreate,
    PatientUpdate,
    PatientResponse
)

router = APIRouter(
    prefix="/patient",
    tags=["Patient"]
)

# ==========================================
# CREATE PATIENT
# ADMIN + STAFF
# ==========================================

@router.post(
    "/",
    response_model=PatientResponse
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    return patient_crud.create_patient(
        db,
        patient
    )


# ==========================================
# READ ALL
# ADMIN + STAFF
# ==========================================

@router.get(
    "/",
    response_model=list[PatientResponse]
)
def read_patient(
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    return patient_crud.get_all_patient(db)


# ==========================================
# READ ONE
# ADMIN + STAFF
# ==========================================

@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def read_patient_id(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    patient = patient_crud.get_patient_by_id(
        db,
        patient_id
    )

    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


# ==========================================
# UPDATE
# ADMIN + STAFF
# ==========================================

@router.put(
    "/{patient_id}",
    response_model=PatientResponse
)
def update_patient(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_staff_or_admin)
):

    result = patient_crud.update_patient(
        db,
        patient_id,
        patient
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return result


# ==========================================
# DELETE
# ADMIN ONLY
# ==========================================

@router.delete(
    "/{patient_id}"
)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_admin_user)
):

    result = patient_crud.delete_patient(
        db,
        patient_id
    )

    if not result:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {

        "message": "Patient deleted successfully"

    }