from repositories.user_repository import UserRepository
from models.user import User, UserInDB
from passlib.context import CryptContext
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def signup(user: User) -> Optional[UserInDB]:
        existing_user = UserRepository.find_by_username(user.username)
        if existing_user:
            return None  # Username already exists

        hashed_password = AuthService.hash_password(user.password)
        user_in_db = UserInDB(username=user.username, hashed_password=hashed_password)
        return UserRepository.create_user(user_in_db)

    @staticmethod
    def login(username: str, password: str) -> bool:
        user_in_db = UserRepository.find_by_username(username)
        if not user_in_db:
            return False
        return AuthService.verify_password(password, user_in_db.hashed_password)

    @staticmethod
    def logout() -> bool:
        # Just a placeholder since there's no session tracking here
        return True
