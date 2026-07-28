from pydantic import BaseModel



class StaffCreate(BaseModel):

    firstname:str
    lastname:str
    position:str
    contact_number:str




class StaffUpdate(BaseModel):

    firstname:str
    lastname:str
    position:str
    contact_number:str




class StaffResponse(BaseModel):

    staff_id:int
    firstname:str
    lastname:str
    position:str
    contact_number:str


    class Config:

        from_attributes=True