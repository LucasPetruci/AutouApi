from app.domains.ai.services import GeminiService
from app.domains.ai.schemas.ai_request import AIRequest
from app.domains.ai.schemas.ai_response import AIResponse

class AIController:
    def __init__(self):
        self.service = GeminiService()
    
    def classify(self, request: AIRequest) -> AIResponse:
        result = self.service.classify_email(request.content)
        return AIResponse(**result)