from fastapi import FastAPI

from app.database import Base, engine


# Import all models first
from app.staff.staff_models import Staff
from app.patient.patient_models import Patient
from app.consultation.consultation_models import Consultation
from app.user import user_models


from fastapi.middleware.cors import CORSMiddleware


# Create database tables
Base.metadata.create_all(bind=engine)



# Import routers
from app.staff.staff_routers import router as staff_router
from app.patient.patient_routers import router as patient_router
from app.consultation.consultation_routers import router as consultation_router
from app.dashboard.dashboard_routers import router as dashboard_router
from app.user.user_routers import router as user_router
from app.auth.auth_routers import router as auth_router


app = FastAPI(
    title="Barangay Health Center System"
)



# Register routers

app.include_router(
    staff_router
)

app.include_router(
    patient_router
)

app.include_router(
    consultation_router
)

app.include_router(
    dashboard_router
)

app.include_router(
    user_router
)

app.include_router(
    auth_router
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

