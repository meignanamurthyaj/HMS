from pydantic import BaseModel
from datetime import date 

class Create_Doctor(BaseModel):
    Doctor_name : str
    Specialization : str
    email : str

class Create_Patient(BaseModel):
    Doctor_id : int
    Patient_name : str 
    Disease : str
    Appointment_date : date
    Patient_status : str

class Update_status(BaseModel):
    Patient_status: str