from pydantic import BaseModel
from datetime import date, time


# ==========================================
# Patient (Nested)
# ==========================================

class PatientInfo(BaseModel):

    patient_id: int

    firstname: str

    lastname: str

    class Config:

        from_attributes = True


# ==========================================
# Create
# ==========================================

class ConsultationCreate(BaseModel):

    diagnosis: str

    medicine: str

    consultation_date: date

    consultation_time: time

    patient_id: int


# ==========================================
# Update
# ==========================================

class ConsultationUpdate(BaseModel):

    diagnosis: str

    medicine: str

    consultation_date: date

    consultation_time: time


# ==========================================
# Response
# ==========================================

class ConsultationResponse(BaseModel):

    consultation_id: int

    diagnosis: str

    medicine: str

    consultation_date: date

    consultation_time: time

    patient_id: int

    patient: PatientInfo

    class Config:

        from_attributes = True