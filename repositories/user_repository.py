
from passlib.context import CryptContext
from pydantic import BaseModel

class User(BaseModel):
    username: str
    hashed_password: str

#NOTE! hashing is not the responsibility of user_repository, therefore in an actual application the below line would not exist
#it is included here only to add a dummy user to the mock database for testing purposes
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Mock database
db = [User(username="username", hashed_password=pwd_context.hash("password"))]

class UserRepository:
    @staticmethod
    def create_user(username, hashed_password):
        user = User(username=username, hashed_password=hashed_password)
        db.append(user)
        return user

    @staticmethod
    def find_by_username(username: str):
        for user in db:
            if user.username == username:
                return user
        return None
