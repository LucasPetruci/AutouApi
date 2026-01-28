from app.domains.ai.services.gemini_service import GeminiService
from app.domains.file.services.file_processor_service import FileProcessorService
from app.exceptions.classifier_exceptions import ClassifierException
from app.exceptions.file_exceptions import EmptyContentException

class ClassifierService:
    def __init__(self):
        self.ai_service = GeminiService()
        self.file_service = FileProcessorService()
    
    def classify_text(self, content: str) -> dict:
        if not content or not content.strip():
            raise EmptyContentException("Email content is empty")
        
        try:
            result = self.ai_service.classify_email(content)
            return result
        except Exception as e:
            raise ClassifierException(f"Error classifying email: {str(e)}")
    
    def classify_file(self, file, filename: str) -> dict:
        file_size = len(file.read())
        file.seek(0)
        
        self.file_service.validate_file_size(file_size)
        
        content = self.file_service.extract_text(file, filename)
        
        classification = self.classify_text(content)
        
        return {
            "filename": filename,
            "size": file_size,
            "content_extracted": content[:500] + "..." if len(content) > 500 else content,
            "classification": classification
        }
