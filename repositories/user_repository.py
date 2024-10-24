from models.user import UserInDB

# Mock database
db = []

class UserRepository:
    @staticmethod
    def create_user(user: UserInDB):
        db.append(user)
        return user

    @staticmethod
    def find_by_username(username: str):
        for user in db:
            if user.username == username:
                return user
        return None
