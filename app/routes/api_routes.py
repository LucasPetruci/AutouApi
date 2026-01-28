from fastapi import APIRouter, UploadFile, File, HTTPException
from app.domains.classifier.controllers import ClassifierController
from app.domains.classifier.schemas import (
    EmailClassifyRequest,
    EmailClassifyResponse,
    EmailFileUploadResponse
)

router = APIRouter(prefix="/api", tags=["Email Classifier"])
classifier_controller = ClassifierController()

@router.post("/classify/text", response_model=EmailClassifyResponse)
async def classify_text(request: EmailClassifyRequest):

    try:
        return classifier_controller.classify_text(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/classify/file", response_model=EmailFileUploadResponse)
async def classify_file(file: UploadFile = File(...)):
    try:
        return await classifier_controller.classify_file(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
