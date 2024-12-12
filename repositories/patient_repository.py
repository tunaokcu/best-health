from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: int
    name: str
    date_of_birth: str
    address: str
    contact: str
    medical_history: Optional[str]
    room_number: Optional[int]

# Mock database for patients
db_patients = [
    Patient(id=1, name="John Doe", date_of_birth="1985-08-15", address="123 Main St", contact="123-456-7890", medical_history="No major issues"),
    Patient(id=2, name="Jane Smith", date_of_birth="1990-05-22", address="456 Oak St", contact="987-654-3210", medical_history="Asthma", room_number=1)
]

class PatientRepository:
    @staticmethod 
    def set_occupied_room(patient_id:int, room_number=None):
        db_patients[patient_id - 1].room_number = room_number

    @staticmethod
    def create_patient(name: str, date_of_birth: str, address: str, contact: str, medical_history: str = None):
        patient = Patient(id=len(db_patients) + 1, name=name, date_of_birth=date_of_birth, address=address, contact=contact, medical_history=medical_history)
        db_patients.append(patient)
        return patient

    @staticmethod
    def find_by_id(patient_id: int):
        """
        Find a patient by their unique ID.
        """
        if patient_id <= 0 or patient_id > len(db_patients):
            return None
        return db_patients[patient_id - 1]

    @staticmethod
    def find_by_contact(contact: str):
        """
        Find a patient by their contact number.
        """
        for patient in db_patients:
            if patient.contact == contact:
                return patient
        return None

    @staticmethod
    async def update_patient(patient_id: int, name: str = None, date_of_birth: str = None, address: str = None, contact: str = None, medical_history: str = None):
        patient = await PatientRepository.find_by_id(patient_id)
        if not patient:
            return None
        
        # Update only the fields provided, leave others unchanged
        name = name or patient.name
        date_of_birth = date_of_birth or patient.date_of_birth
        address = address or patient.address
        contact = contact or patient.contact
        medical_history = medical_history or patient.medical_history

        updated_patient = Patient(id=patient_id, name=name, date_of_birth=date_of_birth, address=address, contact=contact, medical_history=medical_history)
        db_patients[patient_id - 1] = updated_patient

        return updated_patient

    @staticmethod
    async def search(name: str = None, contact: str = None):
        """
        Search for patients by name or contact.
        """
        results = []
        if name:
            results.extend([patient for patient in db_patients if name.lower() in patient.name.lower()])
        if contact:
            results.extend([patient for patient in db_patients if contact in patient.contact])

        return results
