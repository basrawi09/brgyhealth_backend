from app.database import SessionLocal
from app.user.user_models import User
from app.auth.auth_security import hash_password

from app.staff.staff_models import Staff
from app.patient.patient_models import Patient
from app.consultation.consultation_models import Consultation

db = SessionLocal()

user = db.query(User).filter(User.username == "admin1").first()

if user:
    user.password_hash = hash_password("admin123")
    db.commit()
    print("Password updated successfully!")
else:
    print("User not found.")

db.close()