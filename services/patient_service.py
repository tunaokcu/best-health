from repositories.patient_repository import PatientRepository

class PatientService:
    @staticmethod
    def register_patient(name: str, date_of_birth: str, address: str, contact: str, medical_history: str = None):
        """
        Register a new patient.
        """
        # Check if a patient with the same contact already exists
        existing_patient = PatientRepository.find_by_contact(contact)
        if existing_patient:
            return None  # Patient with this contact already exists

        # Create and return the patient record
        return PatientRepository.create_patient(name, date_of_birth, address, contact, medical_history)

    @staticmethod
    def get_patient_details(patient_id: int):
        """
        Retrieve patient details by ID.
        """
        # Fetch patient details from the repository
        return PatientRepository.find_by_id(patient_id)

    @staticmethod
    def update_patient(patient_id: int, name: str, date_of_birth: str, address: str, contact: str, medical_history: str = None):
        """
        Update an existing patient's details.
        """
        # Check if the patient exists
        patient = PatientRepository.find_by_id(patient_id)
        if not patient:
            return None  # Patient not found

        # Update and return the updated record
        return PatientRepository.update_patient(patient_id, name, date_of_birth, address, contact, medical_history)

    @staticmethod
    def search_patients(name: str = None, contact: str = None):
        """
        Search patients by name or contact.
        """
        # Search for patients in the repository
        return PatientRepository.search(name=name, contact=contact)
