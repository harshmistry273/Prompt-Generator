# IMPORTS
from fastapi import BackgroundTasks
from app.core.logging import logger
from app.crud.otp import OTPCRUD
from app.exceptions.base_exceptions import AppException
from app.exceptions.database_exceptions import DataBaseException


# BUSINESS LOGIC FOR USERS
class OTPService:
    
    # SERVICE FOR STORING OTP
    def store_otp(self, otp: str, user_id):
        try:
            otp_data = {"otp": otp, "user_id": user_id}
            OTPCRUD.create_otp(otp_data)

            logger.info("OTP stored")
            
            return True

        except DataBaseException:
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise AppException(message=f"Unexpected error: {e}")
