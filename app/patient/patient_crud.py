from sqlalchemy.orm import Session

from .patient_models import Patient
from .patient_schemas import PatientCreate, PatientUpdate


# CREATE
def create_patient(
    db: Session,
    patient: PatientCreate
):

    new_patient = Patient(
        firstname=patient.firstname,
        lastname=patient.lastname,
        age=patient.age,
        address=patient.address,
        contact_number=patient.contact_number,
        staff_id=patient.staff_id
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


# READ ALL
def get_all_patient(db: Session):

    return db.query(Patient).all()


# READ ONE
def get_patient_by_id(
    db: Session,
    patient_id: int
):

    return (
        db.query(Patient)
        .filter(Patient.patient_id == patient_id)
        .first()
    )


# UPDATE
def update_patient(
    db: Session,
    patient_id: int,
    patient: PatientUpdate
):

    existing = get_patient_by_id(db, patient_id)

    if existing is None:
        return None

    existing.firstname = patient.firstname
    existing.lastname = patient.lastname
    existing.age = patient.age
    existing.address = patient.address
    existing.contact_number = patient.contact_number

    # Update staff_id if your schema contains it
    if hasattr(patient, "staff_id"):
        existing.staff_id = patient.staff_id

    db.commit()
    db.refresh(existing)

    return existing


# DELETE
def delete_patient(
    db: Session,
    patient_id: int
):

    existing = get_patient_by_id(db, patient_id)

    if existing is None:
        return None

    db.delete(existing)
    db.commit()

    return existing