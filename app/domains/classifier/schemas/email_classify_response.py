from pydantic import BaseModel, Field
from datetime import datetime

class EmailClassifyResponse(BaseModel):
    category: str = Field(..., description="Productive or Unproductive")
    confidence: float = Field(..., ge=0, le=1)
    suggested_response: str
    reasoning: str
    processed_at: datetime = Field(default_factory=datetime.now)
