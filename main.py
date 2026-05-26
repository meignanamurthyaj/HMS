from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Doctor, Patients
from schemas import Create_Doctor, Create_Patient, Update_status

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

Base.metadata.create_all(bind = engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FRONTEND HTML ROUTES

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/doctor-registration", response_class=HTMLResponse)
def doctor_page(request: Request):
    return templates.TemplateResponse(request=request, name="doctor.html")

@app.get("/patient-registration", response_class=HTMLResponse)
def patient_page(request: Request):
    return templates.TemplateResponse(request=request, name="patient.html")

@app.get("/view-doctors", response_class=HTMLResponse)
def view_doctors_page(request: Request):
    return templates.TemplateResponse(request=request, name="view_doctors.html")

@app.get("/view-patients", response_class=HTMLResponse)
def view_patients_page(request: Request):
    return templates.TemplateResponse(request=request, name="view_patients.html")

# BACKEND API ROUTES


# Add Doctor
@app.post("/add_Doctor")
def add_Doctor(doctor: Create_Doctor, db: Session = Depends(get_db)):
    try:
        new_Doctor = Doctor(
            Doctor_name = doctor.Doctor_name,
            Specialization = doctor.Specialization,
            email = doctor.email    
        )
        db.add(new_Doctor)
        db.commit()
        db.refresh(new_Doctor)
        return{"message": "Doctor Added Successfully"}
    except Exception as e:
        return{"error":str(e)}

# View All Doctors
@app.get("/Doctor")
def get_Doctor(db: Session = Depends(get_db)):
    return db.query(Doctor).all()

# Add Patient
@app.post("/add_Patient")
def add_Patient(patient: Create_Patient, db: Session = Depends(get_db)):
    try:
        new_Patient = Patients(
            Doctor_id = patient.Doctor_id,
            Patient_name = patient.Patient_name,
            Disease = patient.Disease,
            Appointment_date = patient.Appointment_date,   
            Patient_status = patient.Patient_status
        )
        db.add(new_Patient)
        db.commit()
        db.refresh(new_Patient)
        return{"message": "Patient Added Successfully"}
    except Exception as e:
        return{"error":str(e)}

# View All Patients (WITH SQL JOIN)
@app.get("/Patients")
def get_Patients(db: Session = Depends(get_db)):
    results = db.query(Patients, Doctor).join(Doctor, Patients.Doctor_id == Doctor.Doctor_id).all()
    
    patient_list = []
    for patient, doctor in results:
        patient_list.append({
            "Patient_id": patient.Patient_id,
            "Doctor_name": doctor.Doctor_name,
            "Patient_name": patient.Patient_name,
            "Disease": patient.Disease,
            "Appointment_date": patient.Appointment_date,
            "Patient_status": patient.Patient_status
        })
    return patient_list

# Search Patient by Doctor ID
@app.get("/Patient/{Doctor_id}")
def get_Patients_by_doctor(Doctor_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patients).filter(Patients.Doctor_id == Doctor_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    return patient

# Update Patient Status
@app.put("/update_Patient_status/{Patient_id}")
def update_Patient_status(Patient_id: int, data: Update_status, db: Session = Depends(get_db)):
    Patient = db.query(Patients).filter(Patients.Patient_id == Patient_id).first()
    if Patient is None:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    
    Patient.Patient_status = data.Patient_status
    db.commit()
    return {"message": "Patients Status Updated Successfully"}

# Delete Patient Record
@app.delete("/delete_Patient/{Patient_id}")
def delete_Patient(Patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patients).filter(Patients.Patient_id == Patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    
    db.delete(patient)
    db.commit()
    return {"message": "Patients Record Deleted Successfully"}