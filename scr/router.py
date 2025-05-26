from fastapi import APIRouter, HTTPException
from scr.classifier.model import MODEL_NAME, classifier
from scr.schemas import TextRequestSchema


router = APIRouter(prefix="")


@router.get("/health/")
async def health_check():
    return {"status": "ok", "model": MODEL_NAME}


@router.post("/classify/")
async def classify_text(request: TextRequestSchema):
    try:
        result = classifier(request.text)
        return {"text": request.text, "prediction": result[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
