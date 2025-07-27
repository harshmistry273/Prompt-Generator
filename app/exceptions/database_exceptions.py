from app.exceptions.base_exceptions import AppException
from fastapi import status

class DataBaseException(AppException):
    def __init__(self, message: str = "An error occurred", status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)