from pydantic import BaseModel, Field

class FileUploadResponse(BaseModel):
    filename: str = Field(..., description="File name")
    size: int = Field(..., description="Size in bytes")
    content: str = Field(..., description="Extracted content")
    extension: str = Field(..., description="File extension")