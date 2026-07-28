from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from . import dashboard_crud

from .dashboard_schemas import (
    DashboardStats,
    ConsultationPerPatient,
    StaffPositionDistribution,
    DashboardRecent,
    TodaySchedule,
    WeeklyConsultation,
    TopDiagnosis
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


# ==========================================
# Dashboard Statistics
# ==========================================
@router.get(
    "/stats",
    response_model=DashboardStats
)
def dashboard_stats(
    db: Session = Depends(get_db)
):

    return dashboard_crud.get_dashboard_stats(db)


# ==========================================
# Consultations Per Patient
# ==========================================
@router.get(
    "/consultations-per-patient",
    response_model=list[ConsultationPerPatient]
)
def consultations_per_patient(
    db: Session = Depends(get_db)
):

    return dashboard_crud.get_consultations_per_patient(db)


# ==========================================
# Staff Position Distribution
# ==========================================
@router.get(
    "/staff-position-distribution",
    response_model=list[StaffPositionDistribution]
)
def staff_position_distribution(
    db: Session = Depends(get_db)
):

    return dashboard_crud.get_staff_position_distribution(db)


# ==========================================
# Weekly Consultation Analytics
# ==========================================
@router.get(
    "/weekly-consultations",
    response_model=list[WeeklyConsultation]
)
def weekly_consultations(
    db: Session = Depends(get_db)
):

    return dashboard_crud.get_weekly_consultations(db)


# ==========================================
# Top Diagnoses
# ==========================================
@router.get(
    "/top-diagnoses",
    response_model=list[TopDiagnosis]
)
def top_diagnoses(
    db: Session = Depends(get_db)
):

    return dashboard_crud.get_top_diagnoses(db)


# ==========================================
# Recent Activity
# ==========================================
@router.get(
    "/recent",
    response_model=DashboardRecent
)
def recent_activity(
    db: Session = Depends(get_db)
):

    return dashboard_crud.get_recent_activity(db)


# ==========================================
# Today's Consultation Schedule
# ==========================================
@router.get(
    "/today-schedule",
    response_model=list[TodaySchedule]
)
def today_schedule(
    db: Session = Depends(get_db)
):

    return dashboard_crud.get_today_schedule(db)