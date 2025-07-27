from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.core.logging import logger
from app.exceptions.base_exceptions import AppException
from app.exceptions.database_exceptions import DataBaseException
from app.exceptions.user_exceptions import UserAlreadyExists
from app.schemas.user import CreateUser
from app.services.user import UserService


router = APIRouter()


@router.post("/create-user")
def create_user(user_data: CreateUser):
    try:
        new_user = UserService.register_user(user_data=user_data)
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
                "message": "DB Error",
                "data": [],
                "status": False,
                "error": e.message
            }
        )