from app.exceptions.base_exceptions import AppException

class FailedTokenException(AppException):
    def __init__(self, message: str = "An error occurred", status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class InvalidPasswordException(AppException):
    def __init__(self, message: str = "Password incorrect", status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)