from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from app.core.logging import logger
from app.exceptions.base_exceptions import AppException
from app.exceptions.auth_exceptions import FailedTokenException, InvalidPasswordException
from app.exceptions.user_exceptions import UserNotFound
from app.schemas.user import LoginUser
from app.services.auth import AuthServices


router = APIRouter()
service = AuthServices()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@router.post("/login", status_code=status.HTTP_200_OK)
def login_user(user_data: LoginUser):
    try:
        access_token = service.login_for_access_token(user_data=user_data)
        logger.info("Sending Response")
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "User Logged In",
                "data": [access_token],
                "status": True,
                "error": None
            }
        )
        
    except FailedTokenException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "message": "Failed to create token",
                "data": [],
                "status": False,
                "error": e.message
            }
        )

    except InvalidPasswordException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "message": "Invalid Password",
                "data": [],
                "status": False,
                "error": e.message
            }
        )
    
    except UserNotFound as e:
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
                "message": "An Error Occured",
                "data": [],
                "status": False,
                "error": e.message
            }
        )