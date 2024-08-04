from fastapi import APIRouter, UploadFile, HTTPException, File, Form, Depends
from sqlalchemy.orm import Session
from pymongo.errors import ConnectionFailure
from app.services.api_service import (
    process_natural_language,
    parse_structures,
    save_specification,
    get_specification,
    check_openai_health
)
from app.models.database import get_db, mongo_db
from app.schemas.api_schemas import APIGenerationRequest, APIGenerationResponse, APIUploadResponse
from app.services.publish_service import handle_request

router = APIRouter()

@router.post("/process_natural_language", response_model=APIGenerationResponse)
async def process_natural_language_endpoint(description: str = Form(...)):
    return await process_natural_language(description)

@router.post("/upload_structures", response_model=APIUploadResponse)
async def upload_structures(request: UploadFile = File(...), response: UploadFile = File(...)):
    return await parse_structures(request, response)

@router.post("/save_specification")
async def save_specification_route(name: str = Form(...), description: str = Form(...), spec_type: str = Form(...), spec: UploadFile = File(...)):
    content = await spec.read()
    if spec_type == 'json':
        spec_data = process_json(content)
    else:
        spec_data = process_yaml(content)
    spec_id = save_specification(name, description, spec_type, spec_data)
    return {"spec_id": spec_id}

@router.get("/get_specification/{spec_id}")
async def get_specification_route(spec_id: str):
    spec = get_specification(spec_id)
    if not spec:
        return {"error": "Specification not found"}
    return {"spec": spec}

@router.get("/healthcheck/postgresql")
async def postgresql_healthcheck(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "detail": str(e)}

@router.get("/healthcheck/mongodb")
async def mongodb_healthcheck():
    try:
        mongo_db.command("ping")
        return {"status": "healthy"}
    except ConnectionFailure as e:
        return {"status": "unhealthy", "detail": str(e)}

@router.get("/healthcheck/openai")
async def openai_healthcheck():
    return await check_openai_health()



@router.api_route("/{project_name}/{api_version}/{endpoint}", methods=["GET", "POST", "PUT", "DELETE"])
async def handle_dynamic_request(project_name: str, api_version: str, endpoint: str, request: Request):
    try:
        response = await handle_request(project_name, api_version, endpoint, request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
