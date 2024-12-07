from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: int
    name: str
    date_of_birth: str
    address: str
    contact: str
    medical_history: Optional[str]


#TODO
class PatientRepository:
    @staticmethod
    def create_patient(name: str, date_of_birth: str, address: str, contact: str, medical_history: str = None):
        """
        Create a new patient record in the database.
        """
        # Placeholder for database insert operation
        pass

    @staticmethod
    def find_by_id(patient_id: int):
        """
        Find a patient by their unique ID.
        """
        # Placeholder for database query
        pass

    @staticmethod
    def find_by_contact(contact: str):
        """
        Find a patient by their contact number.
        """
        # Placeholder for database query
        pass

    @staticmethod
    def update_patient(patient_id: int, name: str, date_of_birth: str, address: str, contact: str, medical_history: str = None):
        """
        Update patient details in the database.
        """
        # Placeholder for database update operation
        pass

    @staticmethod
    def search(name: str = None, contact: str = None):
        """
        Search for patients by name or contact.
        """
        # Placeholder for database search operation
        pass
