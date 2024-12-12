from repositories.room_repository import RoomRepository
from repositories.room_repository import RoomRepository, STATUS_AVAILABLE, STATUS_OCCUPIED

class RoomService:
    @staticmethod
    def is_available(room_id):
        room = RoomRepository.find_by_id(room_id)
        if not room or room.status != STATUS_AVAILABLE:
            return None  
        
    @staticmethod
    def mark_as_available(room_id):
        RoomRepository.update_room_status(room_id, STATUS_AVAILABLE)

    @staticmethod 
    def mark_as_occupied(room_id, occupant_id):
        RoomRepository.update_room_status(room_id, STATUS_OCCUPIED, occupant_id)

    @staticmethod
    def create_room(room_type, description=None):
        return RoomRepository.create_room(room_type, description)

    @staticmethod
    def get_room_by_id(room_id: int):
        return RoomRepository.find_by_id(room_id)

    @staticmethod
    def edit_room(room_id: int, room_type=None, description=None):
        return RoomRepository.edit_room(room_id, room_type, description)

    @staticmethod
    def get_all_rooms():
        return RoomRepository.find_all_rooms()
