from pydantic import BaseModel


# ==========================================
# Dashboard Statistics
# ==========================================
class DashboardStats(BaseModel):

    staff: int
    patients: int
    consultations: int
    users: int


# ==========================================
# Consultation Per Patient
# ==========================================
class ConsultationPerPatient(BaseModel):

    patient: str
    consultations: int


# ==========================================
# Staff Position Distribution
# ==========================================
class StaffPositionDistribution(BaseModel):

    position: str
    count: int


# ==========================================
# Weekly Consultation Analytics
# ==========================================
class WeeklyConsultation(BaseModel):

    day: str
    consultations: int


# ==========================================
# Top Diagnoses
# ==========================================
class TopDiagnosis(BaseModel):

    diagnosis: str
    count: int


# ==========================================
# Recent Staff
# ==========================================
class RecentStaff(BaseModel):

    staff_id: int
    firstname: str
    lastname: str
    position: str

    class Config:

        from_attributes = True


# ==========================================
# Recent Patient
# ==========================================
class RecentPatient(BaseModel):

    patient_id: int
    firstname: str
    lastname: str
    age: int

    class Config:

        from_attributes = True


# ==========================================
# Recent Consultation
# ==========================================
class RecentConsultation(BaseModel):

    consultation_id: int
    diagnosis: str
    consultation_date: str
    consultation_time: str
    patient_id: int


# ==========================================
# Dashboard Recent
# ==========================================
class DashboardRecent(BaseModel):

    staff: list[RecentStaff]
    patients: list[RecentPatient]
    consultations: list[RecentConsultation]


# ==========================================
# Today's Consultation Schedule
# ==========================================
class TodaySchedule(BaseModel):

    consultation_id: int
    time: str
    patient: str
    diagnosis: str