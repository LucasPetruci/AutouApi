from pydantic import BaseModel, Field

class AIRequest(BaseModel):
    content: str = Field(..., min_length=1, description="Email content")
