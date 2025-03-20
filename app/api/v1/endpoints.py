# placeholder
from fastapi import APIRouter, HTTPException
from app.models.schemas import PromptRequest, PromptResponse
from app.services.openai_service import generate_openai_response

router = APIRouter()


@router.post("/generate", response_model=PromptResponse)
async def generate_response(request: PromptRequest):
    try:
        result = await generate_openai_response(request.prompt)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
