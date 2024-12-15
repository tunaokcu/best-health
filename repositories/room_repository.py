from pydantic import BaseModel
from typing import Optional

#Status
STATUS_AVAILABLE = "available"
STATUS_OCCUPIED = "occupied"

#Type
TYPE_ICU = "ICU"
TYPE_GENERAL = "General"
TYPE_PRIVATE = "Private"

class Room(BaseModel):
    id: int            # Room number or unique ID
    status: str        # Status of the room (e.g., "available", "occupied")
    type: str          # Room type (e.g., "ICU", "General", "Private")
    occupant_id: Optional[int] = None# occupant id if status is occupied
    description: Optional[str] = None  # Optional description for the room


# TODO encrypt data
# Mock database
db = [Room(id=1, status=STATUS_OCCUPIED, type=TYPE_ICU, occupant_id=2),
      Room(id=2, status=STATUS_AVAILABLE, type=TYPE_ICU),
      Room(id=3, status=STATUS_AVAILABLE, type=TYPE_GENERAL),
      Room(id=4, status=STATUS_AVAILABLE, type=TYPE_GENERAL),
      Room(id=5, status=STATUS_AVAILABLE, type=TYPE_PRIVATE),
      Room(id=6, status=STATUS_OCCUPIED, type=TYPE_PRIVATE, occupant_id=3)
    ]

class RoomRepository:
    @staticmethod
    def create_room(roomType: str, description=None):
        room = Room(id =len(db)+1, status=STATUS_AVAILABLE, type=roomType, description=description)
        db.insert(room)
        return room 

    @staticmethod
    def find_by_id(room_id: int):
        if len(db) < room_id or room_id <= 0:
            return None 

        return db[room_id-1]

    @staticmethod 
    # Edit room_type and description
    def edit_room(room_id: int, room_type=None, description=None):
        if len(db) < room_id:
            return None 
        
        room = db[room_id-1]
        room_type = room_type or room.type 
        description = room.description

        db[room_id-1] = Room(id=room_id, status=room.status, type=room_type, description=description, occupant_id=room.occupant_id) 
        
    @staticmethod
    def update_room_status(room_id: int, status: str, occupant_id=None):
        print("here")
        if len(db) < room_id:
            return None 
        
        room = db[room_id-1]
        roomType = room.type 
        description = room.description 

        db[room_id-1] = Room(id=room_id, status=status, type=roomType, description=description, occupant_id=occupant_id)

        print(db)

    @staticmethod
    def find_all_rooms():
        return db 
