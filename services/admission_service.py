from repositories.admission_repository import AdmissionRepository
from repositories.room_repository import RoomRepository

class AdmissionService:
    @staticmethod
    def admit_patient(patient_id: int, room_id: int, admission_date: str, reason: str, assigned_doctor: str = None):
        """
        Admit a patient by assigning them to a room.
        """
        # Check if the room is available
        room = RoomRepository.find_by_id(room_id)
        if not room or room.status != "available":
            return None  # Room is not available

        # Create the admission record and update the room status
        admission = AdmissionRepository.create_admission(patient_id, room_id, admission_date, reason, assigned_doctor)
        if admission:
            RoomRepository.update_room_status(room_id, "occupied")
        return admission

    @staticmethod
    def get_admission_details(admission_id: int):
        """
        Retrieve details of a specific admission by ID.
        """
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
        room = RoomRepository.find_by_id(room_id)
        if not room or room.status != "available":
            return None  # Room is not available

        # Update the admission record
        updated_admission = AdmissionRepository.update_admission(admission_id, room_id, admission_date, reason, assigned_doctor)
        if updated_admission:
            RoomRepository.update_room_status(room_id, "occupied")
        return updated_admission

    @staticmethod
    def discharge_patient(admission_id: int):
        """
        Discharge a patient and free up the room.
        """
        # Check if the admission exists
        admission = AdmissionRepository.find_by_id(admission_id)
        if not admission:
            return None  # Admission not found

        # Update the room status to available
        RoomRepository.update_room_status(admission.room_id, "available")

        # Remove or mark the admission as discharged
        return AdmissionRepository.mark_as_discharged(admission_id)
