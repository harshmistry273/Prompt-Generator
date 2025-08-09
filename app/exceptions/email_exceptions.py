from app.exceptions.base_exceptions import AppException

class MailNotSend(AppException):
    def __init__(self, message: str = "Failed to send email", status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message, status_code)