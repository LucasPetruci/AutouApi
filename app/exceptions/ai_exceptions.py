from app.exceptions.base import BaseException

class AIProcessingException(BaseException):
    def __init__(self, message: str = "Error processing with AI"):
        super().__init__(message, status_code=500)

class AIConfigurationException(BaseException):
    def __init__(self, message: str = "AI configuration error"):
        super().__init__(message, status_code=500)