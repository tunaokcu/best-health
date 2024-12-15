from repositories.admission_repository import AdmissionRepository
from services.room_service import RoomService
from services.patient_service import PatientService

class AdmissionService:
    @staticmethod
    def admit_patient(patient_id: int, room_id: int, admission_date: str, reason: str):
        # Check if the room is available
        if not RoomService.is_available(room_id):
            print("room not available")
            return None 

        # Check if the patient is already admitted
        if PatientService.is_admitted(patient_id):
            print("patient is admitted")
            return None

        # Create the admission record 
        admission = AdmissionRepository.create_admission(patient_id, room_id, admission_date, reason)

        # Mark room as occupied
        RoomService.mark_as_occupied(room_id, patient_id)

        # Set the patient's occupied room number
        PatientService.set_occupied_room(patient_id, room_id)

        return admission

    @staticmethod
    def change_room(patient_id: int, room_id: int):
        # Check if the room is available
        if not RoomService.is_available(room_id):
            print("room not available")
            return None 
        
        # Update the admission record 
        # TODO
        
        # Find former room id
        former_room_id = PatientService.get_patient(patient_id).room_number

        # Set former room to unoccupied
        RoomService.mark_as_available(former_room_id)

        # Set new room to occupied
        RoomService.mark_as_occupied(room_id, patient_id)

        # Set the patient's occupied room number
        PatientService.set_occupied_room(patient_id, room_id)


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
            RoomService.mark_as_occupied(room_id)

        return updated_admission

    @staticmethod
    def discharge_patient(patient_id: int):
        # Check if the patient is admitted
        if not PatientService.is_admitted(patient_id):
            return None 

        # Update the room status to available
        RoomService.mark_as_available(PatientService.get_room_number(patient_id))

        # Update patient's room to none
        PatientService.discharge_patient(patient_id)

        return True

    @staticmethod
    def get_all_admissions():
        return AdmissionRepository.find_all_admissions()