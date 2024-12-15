from repositories.patient_repository import PatientRepository

class PatientService:
    #TODO fix
    @staticmethod 
    def is_admitted(patient_id: int):
        patient = PatientRepository.find_by_id(patient_id)

        if not patient: return None

        return patient.room_number != None
    
    @staticmethod
    def get_room_number(patient_id: int):
        patient = PatientRepository.find_by_id(patient_id)

        if not patient: 
            return None 

        return patient.room_number
    
    @staticmethod 
    def set_occupied_room(patient_id:int, room_number:int):
        PatientRepository.set_occupied_room(patient_id, room_number)

    @staticmethod
    def discharge_patient(patient_id:int):
        PatientRepository.set_occupied_room(patient_id, None)

    @staticmethod 
    # TODO 
    def register_patient(name: str, lastName: str, date_of_birth: str, address: str, contact: str, medical_history: str = None):
        # Check if a patient with the same contact already exists
        existing_patient = PatientRepository.find_by_contact(contact)
        if existing_patient:
            return None  # Patient with this contact already exists

        # Create and return the patient record
        return PatientRepository.create_patient(name, lastName, date_of_birth, address, contact, medical_history)

    @staticmethod
    def get_all_patients():
        return PatientRepository.find_all_patients()
    
    @staticmethod
    def get_patient(patient_id: int):
        # Fetch patient details from the repository
        return PatientRepository.find_by_id(patient_id)

    @staticmethod
    def update_patient(patient_id: int, name: str, date_of_birth: str, address: str, contact: str, medical_history: str = None):
        return PatientRepository.update_patient(patient_id, name, date_of_birth, address, contact, medical_history)

    #TODO decide if this is needed
    @staticmethod
    def search_patients(name: str = None, contact: str = None):
        # Search for patients in the repository
        return PatientRepository.search(name=name, contact=contact)
