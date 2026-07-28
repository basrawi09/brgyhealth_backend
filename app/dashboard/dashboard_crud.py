from datetime import date, timedelta

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.staff.staff_models import Staff
from app.patient.patient_models import Patient
from app.consultation.consultation_models import Consultation
from app.user.user_models import User


# ==========================================
# Dashboard Statistics
# ==========================================
def get_dashboard_stats(db: Session):

    return {
        "staff": db.query(Staff).count(),
        "patients": db.query(Patient).count(),
        "consultations": db.query(Consultation).count(),
        "users": db.query(User).count()
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
        .order_by(
            Consultation.consultation_date.desc(),
            Consultation.consultation_time.asc()
        )
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
                "consultation_time": str(item.consultation_time),
                "patient_id": item.patient_id
            }
            for item in recent_consultations
        ]

    }


# ==========================================
# Today's Consultation Schedule
# ==========================================
def get_today_schedule(db: Session):

    today = date.today()

    consultations = (

        db.query(Consultation)

        .join(Patient)

        .filter(
            Consultation.consultation_date == today
        )

        .order_by(
            Consultation.consultation_time.asc()
        )

        .all()

    )

    return [

        {

            "consultation_id": consultation.consultation_id,

            "time": str(consultation.consultation_time),

            "patient":
                f"{consultation.patient.firstname} "
                f"{consultation.patient.lastname}",

            "diagnosis": consultation.diagnosis

        }

        for consultation in consultations

    ]


# ==========================================
# Weekly Consultation Analytics
# ==========================================
def get_weekly_consultations(db: Session):

    today = date.today()

    start_of_week = today - timedelta(days=today.weekday())

    end_of_week = start_of_week + timedelta(days=6)

    results = (

        db.query(

            Consultation.consultation_date,

            func.count(
                Consultation.consultation_id
            ).label("count")

        )

        .filter(

            Consultation.consultation_date >= start_of_week,

            Consultation.consultation_date <= end_of_week

        )

        .group_by(
            Consultation.consultation_date
        )

        .all()

    )

    counts = {

        row.consultation_date: row.count

        for row in results

    }

    weekly_data = []

    for i in range(7):

        current_day = start_of_week + timedelta(days=i)

        weekly_data.append({

            "day": current_day.strftime("%a"),

            "consultations": counts.get(current_day, 0)

        })

    return weekly_data

# ==========================================
# Top Diagnoses
# ==========================================
def get_top_diagnoses(db: Session):

    results = (

        db.query(

            Consultation.diagnosis,

            func.count(
                Consultation.consultation_id
            ).label("count")

        )

        .group_by(
            Consultation.diagnosis
        )

        .order_by(
            func.count(
                Consultation.consultation_id
            ).desc()
        )

        .limit(5)

        .all()

    )

    return [

        {

            "diagnosis": row.diagnosis,

            "count": row.count

        }

        for row in results

    ]