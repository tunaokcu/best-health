from repositories.room_repository import RoomRepository

class RoomService:
    @staticmethod
    async def create_room(room):
        """
        Create a new room in the database.
        """
        return await RoomRepository.create_room(room)

    @staticmethod
    async def get_room_by_id(room_id: int):
        """
        Retrieve room details by room ID.
        """
        return await RoomRepository.find_by_id(room_id)

    @staticmethod
    async def update_room(room_id: int, room):
        """
        Update details of an existing room.
        """
        return await RoomRepository.update_room(room_id, room)

    @staticmethod
    async def update_room_status(room_id: int, status: str):
        """
        Update the status of a room.
        """
        return await RoomRepository.update_room_status(room_id, status)

    @staticmethod
    async def get_all_rooms():
        """
        Retrieve all rooms from the database.
        """
        return await RoomRepository.find_all_rooms()
