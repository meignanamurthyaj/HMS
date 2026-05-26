from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base

class Doctor(Base):
    __tablename__ = "Doctors"

    Doctor_id = Column(Integer, primary_key = True, index = True)
    Doctor_name = Column(String(100))
    Specialization = Column(String(100))
    email = Column(String(100))

class Patients(Base):
    __tablename__ = "Patient"
    
    Patient_id = Column(Integer, primary_key = True, index = True)
    Doctor_id = Column(Integer, ForeignKey("Doctors.Doctor_id"))
    Patient_name = Column(String(100))
    Disease = Column(String(100))
    Appointment_date = Column(Date)
    Patient_status = Column(String(100))