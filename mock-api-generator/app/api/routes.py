
from fastapi import APIRouter, UploadFile, File, Form
from app.api.services import process_natural_language, parse_structures, generate_suggestions, finalize_api, publish_api, test_api, generate_api
from app.api.schemas import APIGenerationRequest, APIGenerationResponse, APIUploadResponse

router = APIRouter()

@router.post("/process_natural_language", response_model=APIGenerationResponse)
async def process_natural_language(description: str = Form(...)):
    return await process_natural_language(description)

@router.post("/upload_structures", response_model=APIUploadResponse)
async def upload_structures(request: UploadFile = File(...), response: UploadFile = File(...)):
    return await parse_structures(request, response)

@router.post("/generate_suggestions", response_model=APIGenerationResponse)
async def generate_suggestions(request: APIGenerationRequest):
    return await generate_suggestions(request)

@router.post("/finalize_api", response_model=APIGenerationResponse)
async def finalize_api(request: APIGenerationRequest):
    return await finalize_api(request)

@router.post("/publish_api", response_model=APIUploadResponse)
async def publish_api(api_id: str):
    return await publish_api(api_id)

@router.post("/test_api")
async def test_api(api_id: str, request_data: dict):
    return await test_api(api_id, request_data)

@router.post("/generate")
async def generate_api_endpoint(request: APIGenerationRequest):
    return await generate_api(request)