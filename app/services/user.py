# IMPORTS
from fastapi import BackgroundTasks
from app.core.logging import logger
from app.crud.user import UserCRUD
from app.exceptions.base_exceptions import AppException
from app.exceptions.database_exceptions import DataBaseException
from app.exceptions.user_exceptions import UserAlreadyExists
from app.schemas.user import CreateUser, LoginUser
from app.utils.passwords import PasswordManager


# BUSINESS LOGIC FOR USERS
class UserService:
    
    # SERVICE FOR USER REGISTRATION
    def register_user(self, user_data: CreateUser):
        try:
            # CONVERT DATA TO DICT
            user_data: dict = user_data.model_dump()
            
            # GET USER IF EXISTS
            existing_user = UserCRUD.get_user_by_email(email = user_data.get("email"))
            
            if existing_user:
                logger.error("User already exists")
                raise UserAlreadyExists(status_code=400,
                                    message="User already exists.")
            
            user_data["password"] = PasswordManager.get_password_hash(password=user_data.get("password"))
            
            new_user = UserCRUD.create_user(user_data=user_data)

            logger.info("User created")
            
            return new_user

        except DataBaseException:
            raise
        
        except UserAlreadyExists:
            raise
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise AppException(message=f"Unexpected error: {e}")
