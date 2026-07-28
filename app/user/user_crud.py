from sqlalchemy.orm import Session

from .user_models import User
from .user_schemas import UserCreate, UserUpdate
from app.auth.auth_security import hash_password



# ==========================================
# Get All Users
# ==========================================

def get_users(db: Session):

    return db.query(User).all()


# ==========================================
# Get User by ID
# ==========================================

def get_user(db: Session, user_id: int):

    return (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )


# ==========================================
# Create User
# ==========================================

def create_user(
    db: Session,
    user: UserCreate
):

    try:

        db_user = User(
            username=user.username,
            password_hash=hash_password(user.password),
            role=user.role,
            is_active=True,
            staff_id=user.staff_id
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except Exception as e:

        db.rollback()

        raise Exception(str(e))


# ==========================================
# Update User
# ==========================================

def update_user(
    db: Session,
    user_id: int,
    updated_user: UserUpdate
):

    db_user = get_user(db, user_id)

    if not db_user:

        return None

    db_user.username = updated_user.username

    db_user.role = updated_user.role

    db_user.is_active = updated_user.is_active

    db.commit()

    db.refresh(db_user)

    return db_user


# ==========================================
# Delete User
# ==========================================

def delete_user(
    db: Session,
    user_id: int
):

    db_user = get_user(db, user_id)

    if not db_user:

        return None

    db.delete(db_user)

    db.commit()

    return db_user

# ==========================================
# Toggle User Status
# ==========================================

def toggle_user_status(
    db: Session,
    user_id: int
):

    user = get_user(db, user_id)

    if not user:

        return None

    user.is_active = not user.is_active

    db.commit()

    db.refresh(user)

    return user