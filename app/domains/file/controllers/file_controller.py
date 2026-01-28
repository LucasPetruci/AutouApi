from typing import BinaryIO
from app.domains.file.services import FileProcessorService
from app.domains.file.schemas.file_upload_response import FileUploadResponse

class FileController:
    def __init__(self):
        self.service = FileProcessorService()
    
    def process_file(self, file: BinaryIO, filename: str) -> dict:
        file_size = len(file.read())
        file.seek(0)
        
        self.service.validate_file_size(file_size)
        extension = self.service.validate_file_extension(filename)
        content = self.service.extract_text(file, filename)
        
        return {
            "filename": filename,
            "size": file_size,
            "content": content,
            "extension": extension
        }