from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from app.database import Base



class Staff(Base):

    __tablename__ = "staff"


    staff_id = Column(
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


    position = Column(
        String(50),
        nullable=False
    )


    contact_number = Column(
        String(20),
        nullable=False
    )


    patients = relationship(
        "Patient",
        back_populates="staff"
    )

    user = relationship(
    "User",
    back_populates="staff",
    uselist=False
)