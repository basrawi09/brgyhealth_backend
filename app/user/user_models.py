from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(20),
        nullable=False,
        default="staff"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    staff_id = Column(
        Integer,
        ForeignKey("staff.staff_id"),
        unique=True,
        nullable=False
    )

    staff = relationship(
        "Staff",
        back_populates="user"
    )