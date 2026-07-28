from sqlalchemy import func
from sqlalchemy.orm import Session

from app.staff.staff_models import Staff
from app.patient.patient_models import Patient
from app.consultation.consultation_models import Consultation


# ==========================================
# Dashboard Statistics
# ==========================================
def get_dashboard_stats(db: Session):

    return {
        "staff": db.query(Staff).count(),
        "patients": db.query(Patient).count(),
        "consultations": db.query(Consultation).count()
    }


# ==========================================
# Consultations Per Patient
# ==========================================
def get_consultations_per_patient(db: Session):

    results = (
        db.query(
            Patient.patient_id,
            Patient.firstname,
            Patient.lastname,
            func.count(Consultation.consultation_id).label("consultations")
        )
        .outerjoin(
            Consultation,
            Patient.patient_id == Consultation.patient_id
        )
        .group_by(
            Patient.patient_id,
            Patient.firstname,
            Patient.lastname
        )
        .order_by(
            Patient.patient_id
        )
        .all()
    )

    return [
        {
            "patient": f"{row.firstname} {row.lastname}",
            "consultations": row.consultations
        }
        for row in results
    ]


# ==========================================
# Staff Position Distribution
# ==========================================
def get_staff_position_distribution(db: Session):

    results = (
        db.query(
            Staff.position,
            func.count(Staff.staff_id).label("count")
        )
        .group_by(
            Staff.position
        )
        .order_by(
            Staff.position
        )
        .all()
    )

    return [
        {
            "position": row.position,
            "count": row.count
        }
        for row in results
    ]


# ==========================================
# Recent Activity
# ==========================================
def get_recent_activity(db: Session):

    recent_staff = (
        db.query(Staff)
        .order_by(Staff.staff_id.desc())
        .limit(5)
        .all()
    )

    recent_patients = (
        db.query(Patient)
        .order_by(Patient.patient_id.desc())
        .limit(5)
        .all()
    )

    recent_consultations = (
        db.query(Consultation)
        .order_by(Consultation.consultation_id.desc())
        .limit(5)
        .all()
    )

    return {

        "staff": recent_staff,

        "patients": recent_patients,

        "consultations": [
            {
                "consultation_id": item.consultation_id,
                "diagnosis": item.diagnosis,
                "consultation_date": str(item.consultation_date),
                "patient_id": item.patient_id
            }
            for item in recent_consultations
        ]

    }