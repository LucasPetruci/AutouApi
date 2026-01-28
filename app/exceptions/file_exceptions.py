from app.exceptions.base import BaseException

class InvalidFileTypeException(BaseException):
    def __init__(self, message: str = "Invalid file type"):
        super().__init__(message, status_code=400)

class FileTooLargeException(BaseException):
    def __init__(self, message: str = "File too large"):
        super().__init__(message, status_code=413)

class EmptyContentException(BaseException):
    def __init__(self, message: str = "Empty content"):
        super().__init__(message, status_code=400)