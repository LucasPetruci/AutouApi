from pydantic import BaseModel
from app.domains.classifier.schemas import EmailClassifyResponse

class EmailFileUploadResponse(BaseModel):
    filename: str
    size: int
    content_extracted: str
    classification: EmailClassifyResponse