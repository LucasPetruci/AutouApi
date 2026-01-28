import os
from typing import BinaryIO
from dotenv import load_dotenv
from pypdf import PdfReader
from app.exceptions.file_exceptions import (
    InvalidFileTypeException,
    FileTooLargeException,
    EmptyContentException
)

load_dotenv()

class FileProcessorService:
    def __init__(self):
        self.max_file_size_mb = int(os.getenv("MAX_FILE_SIZE_MB", 10))
        self.allowed_extensions = os.getenv("ALLOWED_EXTENSIONS", "txt,pdf").split(",")
    
    def validate_file_size(self, file_size: int) -> None:
        max_size_bytes = self.max_file_size_mb * 1024 * 1024
        if file_size > max_size_bytes:
            raise FileTooLargeException(
                f"File too large. Maximum size: {self.max_file_size_mb}MB"
            )
    
    def validate_file_extension(self, filename: str) -> str:
        extension = filename.lower().split('.')[-1]
        if extension not in self.allowed_extensions:
            raise InvalidFileTypeException(
                f"Invalid file type. Allowed: {', '.join(self.allowed_extensions)}"
            )
        return extension
    
    def extract_text(self, file: BinaryIO, filename: str) -> str:
        extension = self.validate_file_extension(filename)
        
        if extension == 'txt':
            return self._extract_from_txt(file)
        elif extension == 'pdf':
            return self._extract_from_pdf(file)
        else:
            raise InvalidFileTypeException(f"Unsupported extension: {extension}")
    
    def _extract_from_txt(self, file: BinaryIO) -> str:
        try:
            content = file.read()
            
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    return content.decode(encoding)
                except UnicodeDecodeError:
                    continue
            
            return content.decode('utf-8', errors='ignore')
            
        except Exception as e:
            raise EmptyContentException(f"Error reading TXT file: {str(e)}")
    
    def _extract_from_pdf(self, file: BinaryIO) -> str:
        try:
            pdf_reader = PdfReader(file)
            
            text_parts = []
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    text_parts.append(text)
            
            if not text_parts:
                raise EmptyContentException("Could not extract text from PDF")
            
            return '\n'.join(text_parts)
            
        except Exception as e:
            raise EmptyContentException(f"Error reading PDF file: {str(e)}")