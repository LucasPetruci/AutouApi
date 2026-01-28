from pydantic import BaseModel, Field

class AIResponse(BaseModel):
    category: str = Field(..., description="Productive or Unproductive")
    confidence: float = Field(..., ge=0, le=1, description="Classification confidence")
    suggested_response: str = Field(..., description="Automatic response")
    reasoning: str = Field(..., description="Classification explanation")