from pydantic import BaseModel

class Room(BaseModel):
    id: int            # Room number or unique ID
    status: str        # Status of the room (e.g., "available", "occupied")
    type: str          # Room type (e.g., "ICU", "General", "Private")
    description: str   # Optional description for the room



class RoomRepository:
    @staticmethod
    async def create_room(room):
        """
        Create a new room record in the database.
        """
        # Placeholder for database insert operation
        pass

    @staticmethod
    async def find_by_id(room_id: int):
        """
        Retrieve a room record by ID.
        """
        # Placeholder for database query
        pass

    @staticmethod
    async def update_room(room_id: int, room):
        """
        Update room details in the database.
        """
        # Placeholder for database update operation
        pass

    @staticmethod
    async def update_room_status(room_id: int, status: str):
        """
        Update the status of a room in the database (e.g., 'available' or 'occupied').
        """
        # Placeholder for database update operation
        pass

    @staticmethod
    async def find_all_rooms():
        """
        Retrieve all rooms from the database.
        """
        # Placeholder for database query
        pass
