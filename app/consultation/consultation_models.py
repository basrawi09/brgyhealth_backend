from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base



class Consultation(Base):

    __tablename__ = "consultation"


    consultation_id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    diagnosis = Column(
        String(100),
        nullable=False
    )


    medicine = Column(
        String(100),
        nullable=False
    )


    consultation_date = Column(
        Date,
        nullable=False
    )


    patient_id = Column(
        Integer,
        ForeignKey("patient.patient_id"),
        nullable=False
    )



    # Relationship with Patient

    patient = relationship(
        "Patient",
        back_populates="consultations"
    )