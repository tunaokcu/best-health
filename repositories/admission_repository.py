from pydantic import BaseModel
from typing import Optional

class Admission(BaseModel):
    id: Optional[int]  # Automatically assigned by the database
    patient_id: int    # Foreign key referencing the Patient
    room_id: int       # Foreign key referencing the Room
    admission_date: str
    reason: str
    assigned_doctor: Optional[str]

db = [
    Admission(id=1, patient_id=2, room_id=1, admission_date="12/8/2024", reason="Asthma")
]

class AdmissionRepository:
    @staticmethod
    def create_admission(patient_id: int, room_id: int, admission_date: str, reason: str, assigned_doctor: str = None):
        db.insert(
            Admission(id = len(db)+1, patient_id=patient_id, room_id=room_id, admission_date=admission_date, reason=reason, assigned_doctor=assigned_doctor)
        )

    @staticmethod
    def find_by_id(admission_id: int):
        """
        Retrieve an admission record by ID.
        """
        # Placeholder for database query
        pass

    @staticmethod
    def update_admission(admission_id: int, room_id: int, admission_date: str, reason: str, assigned_doctor: str = None):
        """
        Update an admission record in the database.
        """
        # Placeholder for database update operation
        pass

