from pydantic import BaseModel


class DashboardStats(BaseModel):

    staff: int
    patients: int
    consultations: int


class ConsultationPerPatient(BaseModel):

    patient: str
    consultations: int


class StaffPositionDistribution(BaseModel):

    position: str
    count: int


class RecentStaff(BaseModel):

    staff_id: int
    firstname: str
    lastname: str
    position: str


class RecentPatient(BaseModel):

    patient_id: int
    firstname: str
    lastname: str
    age: int


class RecentConsultation(BaseModel):

    consultation_id: int
    diagnosis: str
    consultation_date: str
    patient_id: int


class DashboardRecent(BaseModel):

    staff: list[RecentStaff]
    patients: list[RecentPatient]
    consultations: list[RecentConsultation]