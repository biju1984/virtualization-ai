from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.api_service import process_file

router = APIRouter()

@router.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="File upload is required")
    content = await file.read()
    result = process_file(file.filename, content)
    return {"result": result}
