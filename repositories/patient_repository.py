from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: int
    name: str
    date_of_birth: str
    gender: str
    address: str
    contact: str
    medical_history: Optional[str] = None
    room_number: Optional[int] = None

# Mock database for patients
db_patients = [
    Patient(id=1, name="John Doe", date_of_birth="1985-08-15", gender="male", address="123 Main St", contact="123-456-7890", medical_history="No major issues"),
    Patient(id=2, name="Jane Smith", date_of_birth="1990-05-22", gender="female", address="456 Oak St", contact="987-654-3210", medical_history="Asthma", room_number=1),
    Patient(id=3, name="Emily Johnson", date_of_birth="1978-11-03", gender="female", address="789 Pine St", contact="555-123-4567", medical_history="Diabetes", room_number=6),
    Patient(id=4, name="Michael Brown", date_of_birth="2002-02-17", gender="male", address="101 Maple St", contact="555-987-6543", medical_history="No allergies"),
    Patient(id=5, name="Sarah Lee", date_of_birth="1989-07-25", gender="female", address="202 Birch St", contact="555-876-5432", medical_history="Hypertension"),
    Patient(id=6, name="David Wilson", date_of_birth="1995-01-30", gender="male", address="303 Cedar St", contact="555-432-8765", medical_history="No chronic conditions"),
    Patient(id=7, name="Olivia Martinez", date_of_birth="1982-12-05", gender="female", address="404 Cherry St", contact="555-654-3210", medical_history="High cholesterol"),
    Patient(id=8, name="James Harris", date_of_birth="1975-09-14", gender="male", address="505 Redwood St", contact="555-321-7654", medical_history="Heart disease"),
    Patient(id=9, name="Mia Clark", date_of_birth="1998-03-29", gender="female", address="606 Willow St", contact="555-765-4321", medical_history="Migraines"),
    Patient(id=10, name="Ethan Lewis", date_of_birth="2000-10-11", gender="male", address="707 Elm St", contact="555-987-4321", medical_history="No significant health issues")
]


class PatientRepository:
    @staticmethod 
    def set_occupied_room(patient_id:int, room_number=None):
        db_patients[patient_id - 1].room_number = room_number

    @staticmethod
    def create_patient(name: str, date_of_birth: str, gender:str, address: str, contact: str, medical_history: str = None):
        patient = Patient(id=len(db_patients) + 1, name=name, date_of_birth=date_of_birth, gender=gender, address=address, contact=contact, medical_history=medical_history)
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
    def update_patient(patient_id: int, name: str = None, date_of_birth: str = None, address: str = None, contact: str = None, medical_history: str = None):
        patient = PatientRepository.find_by_id(patient_id)
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
    def search(name: str = None, contact: str = None):
        """
        Search for patients by name or contact.
        """
        results = []
        if name:
            results.extend([patient for patient in db_patients if name.lower() in patient.name.lower()])
        if contact:
            results.extend([patient for patient in db_patients if contact in patient.contact])

        return results

    @staticmethod
    def find_all_patients():
        return db_patients