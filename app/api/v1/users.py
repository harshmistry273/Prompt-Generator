from fastapi import APIRouter, BackgroundTasks, status
from fastapi.responses import JSONResponse

from app.core.logging import logger
from app.exceptions.base_exceptions import AppException
from app.exceptions.database_exceptions import DataBaseException
from app.exceptions.user_exceptions import UserAlreadyExists
from app.schemas.user import CreateUser
from app.services.otp import OTPService
from app.services.user import UserService
from app.utils.email import EmailService


router = APIRouter()
user_service = UserService()
email_service = EmailService()
otp_service = OTPService()

@router.post("/create-user", status_code=status.HTTP_201_CREATED)
def create_user(background_tasks: BackgroundTasks, user_data: CreateUser):
    try:
        new_user = user_service.register_user(user_data=user_data)[0]
        print(new_user)
        
        if new_user:
            otp = email_service.send_mail_background(background_tasks, new_user["email"])
            otp_service.store_otp(otp=otp, user_id=new_user["id"])

        logger.info("Sending Response")
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "User Created",
                "data": [new_user],
                "status": True,
                "error": None
            }
        )

    except DataBaseException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "message": "DB Error",
                "data": [],
                "status": False,
                "error": e.message
            }
        )
    
    except UserAlreadyExists as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "message": "User Error",
                "data": [],
                "status": False,
                "error": e.message
            }
        )
    
    except AppException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "message": "An Exception occured",
                "data": [],
                "status": False,
                "error": str(e)
            }
        )