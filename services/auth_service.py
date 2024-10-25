from repositories.user_repository import UserRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def signup(username: str, password: str):
        existing_user = UserRepository.find_by_username(username)
        if existing_user:
            return None  # Username already exists

        hashed_password = AuthService.hash_password(password)
        return UserRepository.create_user(username, hashed_password)

    @staticmethod
    def login(username: str, password: str) -> bool:
        user = UserRepository.find_by_username(username)
        # Username does not exist
        if not user:
            return False
        
        # Return true if the hashed version of the password matches the one in the database
        return AuthService.verify_password(password, user.hashed_password)

    @staticmethod
    def logout() -> bool:
        # Just a placeholder since there's no session tracking here
        return True
