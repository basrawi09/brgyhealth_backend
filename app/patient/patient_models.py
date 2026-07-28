from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base



class Patient(Base):

    __tablename__ = "patient"


    patient_id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    firstname = Column(
        String(50),
        nullable=False
    )


    lastname = Column(
        String(50),
        nullable=False
    )


    age = Column(
        Integer,
        nullable=False
    )


    address = Column(
        String(100),
        nullable=False
    )


    contact_number = Column(
        String(20),
        nullable=False
    )


    staff_id = Column(
        Integer,
        ForeignKey("staff.staff_id"),
        nullable=False
    )



    # Relationship to Staff
    staff = relationship(
        "Staff",
        back_populates="patients"
    )



    # Relationship to Consultation
    consultations = relationship(
        "Consultation",
        back_populates="patient",
        cascade="all, delete"
    )