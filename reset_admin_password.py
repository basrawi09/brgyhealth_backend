from app.database import SessionLocal
from app.user.user_models import User
from app.auth.auth_security import hash_password

db = SessionLocal()

existing_user = db.query(User).filter(User.username == "admin1").first()

if existing_user:
    print("Admin user already exists.")
else:
    admin = User(
        username="admin1",
        password_hash=hash_password("admin123"),
        role="Admin"
    )

    db.add(admin)
    db.commit()

    print("Admin user created successfully!")

db.close()