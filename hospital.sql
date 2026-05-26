CREATE DATABASE Hospital_db;

USE Hospital_db;

CREATE TABLE Doctors(
Doctor_id INT PRIMARY KEY AUTO_INCREMENT,
Doctor_name VARCHAR(100) NOT NULL,
Specialization VARCHAR(100) NOT NULL,
Email VARCHAR(100) NOT NULL
);

CREATE TABLE Patient(
Patient_id INT PRIMARY KEY AUTO_INCREMENT,
Doctor_id INT,
Patient_name VARCHAR(100),
Disease VARCHAR(100),
Appointment_date DATE,
Patient_status VARCHAR(100),
FOREIGN KEY (Doctor_id) REFERENCES Doctors(Doctor_id)
);

INSERT INTO Doctors(Doctor_name, Specialization, Email) VALUES
("Dr.Sanjay", "Cardiologist", "sanjay@gmail.com"), 
("Dr.Arun", "Neurologist", "arun@gmail.com"),
("Dr.Vinoth", "Orthopedic Surgeon", "vinoth@gmail.com"),
("Dr.Karthik", "ENT Specialist", "karthik@gmail.com")
;

INSERT INTO Patient(Doctor_id, Patient_name, Disease, Appointment_date, Patient_status) VALUES
(3, "Suresh", "Knee Injury", "2026-06-04", "In process"),
(2, "Kumar", "Stroke", "2026-06-01", "Completed"),
(2, "Vignesh", "migraines", "2026-06-02", "pending"),
(1, "Siva", "Chest Pain", "2026-06-05", "In process"),
(3, "Raja", "Low Back Pain", "2026-06-04", "pending")
;

SELECT * FROM Doctors;
SELECT * FROM Patient;
DELETE FROM Doctors WHERE Doctor_id=6;