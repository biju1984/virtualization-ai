from fastapi import APIRouter, HTTPException, Request
from app.services.prompt_service import handle_prompt

router = APIRouter()

@router.post("/process-prompt/")
async def process_prompt(request: Request):
    data = await request.json()
    prompt = data.get("prompt")
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
    result = handle_prompt(prompt)
    return {"result": result}
