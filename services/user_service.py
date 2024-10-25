from services.auth_service import AuthService
from repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def signup(name: str, lastname: str, email:str, password: str, ):
        existing_user = UserRepository.find_by_email(email)
        if existing_user:
            return None  # Username already exists

        hashed_password = AuthService.hash_password(password)
        return UserRepository.create_user(name, lastname, email, hashed_password)

    @staticmethod
    def login(email: str, password: str) -> bool:
        user = UserRepository.find_by_email(email)
        # Username does not exist
        if not user:
            return False
        
        # Return true if the hashed version of the password matches the one in the database
        return AuthService.verify_password(password, user.hashed_password)

    @staticmethod
    def logout() -> bool:
        # Just a placeholder since there's no session tracking here
        return True