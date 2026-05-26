# Hospital Management System

## Setup Instructions

1. **Database Setup:**
   Run the `hospital_db.sql` script in MySQL to create the database and tables. Update your MySQL password in `database.py`.

2. **Install Dependencies:**
   `pip install -r requirements.txt`

3. **Run Application:**
   `uvicorn main:app --reload`

4. **Access the App:**
   Open a browser and go to `http://127.0.0.1:8000/`