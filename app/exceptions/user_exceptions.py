from app.exceptions.base_exceptions import AppException

class UserAlreadyExists(AppException):
    def __init__(self, message: str = "User Already Exists", status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message, status_code)


class UserNotFound(AppException):
    def __init__(self, message: str = "User Not Found", status_code: int = 404):
        self.message = message
        self.status_code = status_code
        super().__init__(message, status_code)
