from models.user import UserInDB
from models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Mock database
db = [UserInDB(username="username", password="password", hashed_password=pwd_context.hash("password"))]

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
