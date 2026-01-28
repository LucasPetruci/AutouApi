from app.exceptions.base import BaseException

class ClassifierException(BaseException):
    def __init__(self, message: str = "Classification error"):
        super().__init__(message, status_code=500)