from passlib.context import CryptContext

class PasswordManager:
    # CLASS VARIABLES
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # METHODS
    @classmethod
    def get_password_hash(cls, password: str):
        return cls._pwd_context.hash(password)

    @classmethod
    def verify_password_hash(cls, password: str, hashed_password: str):
        return cls._pwd_context.verify(password, hashed_password)