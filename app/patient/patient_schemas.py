from pydantic import BaseModel


class PatientCreate(BaseModel):

    firstname:str
    lastname:str
    age:int
    address:str
    contact_number:str
    staff_id:int



class PatientUpdate(BaseModel):

    firstname:str
    lastname:str
    age:int
    address:str
    contact_number:str
    staff_id:int



class PatientResponse(BaseModel):

    patient_id:int
    firstname:str
    lastname:str
    age:int
    address:str
    contact_number:str
    staff_id:int


    class Config:
        from_attributes=True