from sqlalchemy.orm import Session

from .staff_models import Staff
from .staff_schemas import StaffCreate, StaffUpdate



# READ ALL
def get_all_staff(db: Session):

    return db.query(Staff).all()



# READ BY ID
def get_staff_by_id(
    db: Session,
    staff_id: int
):

    return db.query(Staff).filter(
        Staff.staff_id == staff_id
    ).first()



# CREATE
def create_staff(
    db: Session,
    staff: StaffCreate
):

    new_staff = Staff(
        firstname=staff.firstname,
        lastname=staff.lastname,
        position=staff.position,
        contact_number=staff.contact_number
    )


    db.add(new_staff)

    db.commit()

    db.refresh(new_staff)


    return new_staff



# UPDATE
def update_staff(
    db: Session,
    staff_id: int,
    data: StaffUpdate
):

    staff = get_staff_by_id(
        db,
        staff_id
    )


    if not staff:
        return None



    staff.firstname = data.firstname
    staff.lastname = data.lastname
    staff.position = data.position
    staff.contact_number = data.contact_number


    db.commit()

    db.refresh(staff)


    return staff



# DELETE
def delete_staff(
    db: Session,
    staff_id: int
):

    staff = get_staff_by_id(
        db,
        staff_id
    )


    if not staff:
        return None


    db.delete(staff)

    db.commit()


    return staff