from app.database import SessionLocal

# Import all models so SQLAlchemy can resolve relationships
from app.staff.staff_models import Staff
from app.patient.patient_models import Patient
from app.consultation.consultation_models import Consultation
from app.user.user_models import User

from app.auth.auth_security import hash_password

db = SessionLocal()

try:
    existing_user = db.query(User).filter(User.username == "admin1").first()

    if existing_user:
        print("Admin user already exists.")
    else:
        admin = User(
            username="admin1",
            password_hash=hash_password("admin123"),
            role="Admin",
            is_active=True,
            staff_id=None
        )

        db.add(admin)
        db.commit()

        print("✅ Admin user created successfully!")

finally:
    db.close()