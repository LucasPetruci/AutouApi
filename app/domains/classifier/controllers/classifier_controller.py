from fastapi import UploadFile
from app.domains.classifier.services import ClassifierService
from app.domains.classifier.schemas import (
    EmailClassifyRequest,
    EmailClassifyResponse,
    EmailFileUploadResponse
)

class ClassifierController:
    def __init__(self):
        self.service = ClassifierService()
    
    def classify_text(self, request: EmailClassifyRequest) -> EmailClassifyResponse:
        result = self.service.classify_text(
            request.content, 
            request.language or "pt-BR"
        )
        return EmailClassifyResponse(**result)
    
    async def classify_file(self, file: UploadFile, language: str = "pt-BR") -> EmailFileUploadResponse:
        content = await file.read()
        
        import io
        file_obj = io.BytesIO(content)
        
        result = self.service.classify_file(file_obj, file.filename, language)
        return EmailFileUploadResponse(**result)