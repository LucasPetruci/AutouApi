from pydantic import BaseModel, Field
from typing import Optional

class EmailClassifyRequest(BaseModel):
    content: str = Field(..., min_length=1, description="Email content")
    language: Optional[str] = Field(
        default="pt-BR",
        description="Response language: pt-BR, en-US, es-ES"
    )