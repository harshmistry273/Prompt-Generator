# IMPORTS
from app.core.config import settings
from app.crud.user import UserCRUD
from app.exceptions.auth_exceptions import FailedTokenException, InvalidPasswordException
from app.exceptions.base_exceptions import AppException
from app.exceptions.user_exceptions import UserNotFound
from app.schemas.user import LoginUser
from app.utils.passwords import PasswordManager

from datetime import datetime, timedelta
import jwt


class AuthServices:
    
    def create_access_token(self, data: dict):
        try:
            data_to_encode = data.copy()
            expire = datetime.utcnow() + timedelta(minutes=settings.EXPIRES_MINUTES)
            
            data_to_encode.update({"exp": expire})
            encoded_jwt = jwt.encode(payload=data_to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
            
            return encoded_jwt
        
        except Exception as e:
            raise FailedTokenException(message=f"Failed to create token: {str(e)}", status_code=500)
    
    
    def login_for_access_token(self, user_data: LoginUser):
        try:
            user_data = user_data.model_dump()
            
            user = UserCRUD.get_user_by_email(email=user_data["email"])
            
            if not user:
                raise UserNotFound
            
            if not PasswordManager.verify_password_hash(password=user_data["password"], hashed_password= user[0]["password"]):
                raise InvalidPasswordException
            
            access_token = self.create_access_token(data={"sub": user_data["email"]})
            
            return access_token
        
        except UserNotFound:
            raise
        
        except InvalidPasswordException:
            raise
            
        except Exception as e:
            raise AppException(message=f"Unexpected error: {e}")