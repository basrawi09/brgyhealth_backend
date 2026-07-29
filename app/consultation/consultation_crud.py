from datetime import date

from sqlalchemy.orm import Session, joinedload

from .consultation_models import Consultation


# ==========================================
# CREATE
# ==========================================

def create_consultation(
    db: Session,
    data
):

    new_consultation = Consultation(

        diagnosis=data.diagnosis,

        medicine=data.medicine,

        consultation_date=data.consultation_date,

        consultation_time=data.consultation_time,

        patient_id=data.patient_id

    )

    db.add(new_consultation)

    db.commit()

    db.refresh(new_consultation)

    return (

        db.query(Consultation)

        .options(
            joinedload(Consultation.patient)
        )

        .filter(
            Consultation.consultation_id ==
            new_consultation.consultation_id
        )

        .first()

    )


# ==========================================
# READ ALL
# ==========================================

def get_all_consultations(
    db: Session
):

    return (

        db.query(Consultation)

        .options(
            joinedload(Consultation.patient)
        )

        .order_by(
            Consultation.consultation_date.desc(),
            Consultation.consultation_time.asc()
        )

        .all()

    )


# ==========================================
# CALENDAR
# ==========================================

def get_calendar_schedule(
    db: Session,
    selected_date: date
):

    return (

        db.query(Consultation)

        .options(
            joinedload(Consultation.patient)
        )

        .filter(
            Consultation.consultation_date == selected_date
        )

        .order_by(
            Consultation.consultation_time.asc()
        )

        .all()

    )


# ==========================================
# READ ONE
# ==========================================

def get_consultation_by_id(
    db: Session,
    consultation_id: int
):

    return (

        db.query(Consultation)

        .options(
            joinedload(Consultation.patient)
        )

        .filter(
            Consultation.consultation_id ==
            consultation_id
        )

        .first()

    )


# ==========================================
# UPDATE
# ==========================================

def update_consultation(
    db: Session,
    consultation_id: int,
    data
):

    consultation = get_consultation_by_id(
        db,
        consultation_id
    )

    if not consultation:

        return None

    consultation.diagnosis = data.diagnosis

    consultation.medicine = data.medicine

    consultation.consultation_date = data.consultation_date

    consultation.consultation_time = data.consultation_time

    consultation.patient_id = data.patient_id

    db.commit()

    db.refresh(consultation)

    return consultation


# ==========================================
# DELETE
# ==========================================

def delete_consultation(
    db: Session,
    consultation_id: int
):

    consultation = get_consultation_by_id(
        db,
        consultation_id
    )

    if not consultation:

        return None

    db.delete(consultation)

    db.commit()

    return consultation