from fastapi import UploadFile
from app.domains.classifier.services import ClassifierService
from app.domains.classifier.schemas.email_classify_request import EmailClassifyRequest
from app.domains.classifier.schemas.email_classify_response import EmailClassifyResponse
from app.domains.classifier.schemas.email_file_upload_response import EmailFileUploadResponse

class ClassifierController:
    def __init__(self):
        self.service = ClassifierService()
    
    def classify_text(self, request: EmailClassifyRequest) -> EmailClassifyResponse:
        result = self.service.classify_text(request.content)
        return EmailClassifyResponse(**result)
    
    async def classify_file(self, file: UploadFile) -> EmailFileUploadResponse:
        content = await file.read()
        
        import io
        file_obj = io.BytesIO(content)
        
        result = self.service.classify_file(file_obj, file.filename)
        return EmailFileUploadResponse(**result)