from repositories.admission_repository import AdmissionRepository
from services.room_service import RoomService
from services.patient_service import PatientService

class AdmissionService:
    @staticmethod
    def admit_patient(patient_id: int, room_id: int, admission_date: str, reason: str, assigned_doctor: str = None):
        # Check if the room is available
        if not RoomService.is_available(room_id):
            return None 

        # Check if the patient is already admitted
        if PatientService.is_admitted(patient_id):
            return None

        # Create the admission record 
        admission = AdmissionRepository.create_admission(patient_id, room_id, admission_date, reason, assigned_doctor)

        # Mark room as occupied
        RoomService.mark_room_as_occupied(room_id)

        # Set the patient's occupied room number
        PatientService.set_occupied_room(patient_id, room_id)

        return admission

    @staticmethod
    def get_admission_details(admission_id: int):
        return AdmissionRepository.find_by_id(admission_id)

    @staticmethod
    def update_admission(admission_id: int, room_id: int, admission_date: str, reason: str, assigned_doctor: str = None):
        """
        Update details of an existing admission.
        """
        # Check if the admission exists
        admission = AdmissionRepository.find_by_id(admission_id)
        if not admission:
            return None  # Admission not found

        # Check if the room is available
        if not RoomService.is_available(room_id):
            return None 
        
        # Update the admission record
        updated_admission = AdmissionRepository.update_admission(admission_id, room_id, admission_date, reason, assigned_doctor)
        if updated_admission:
            RoomRepository.update_room_status(room_id, "occupied")

        return updated_admission

    @staticmethod
    def discharge_patient(patient_id: int):

        # Check if the patient is admitted
        if not PatientService.is_admitted(patient_id):
            return False 

        # Update the room status to available
        RoomService.mark_as_available(PatientService.get_room_number(patient_id))

        # Remove or mark the admission as discharged
        return AdmissionRepository.mark_as_discharged(admission_id)
