# Add Request here
from fastapi import APIRouter, UploadFile, HTTPException, File, Form, Depends, Request
from sqlalchemy.orm import Session
from pymongo.errors import ConnectionFailure
from app.services.api_service import (
    process_natural_language,
    check_openai_health,
    process_json,
    process_yaml
)
from app.models.database import get_db, mongo_db
from app.schemas.api_schemas import APIGenerationRequest, APIGenerationResponse, APIUploadResponse
from app.services.publish_service import handle_request
from app.services.workflow_service import WorkflowService

router = APIRouter()


@router.post("/process_natural_language")
async def process_natural_language_endpoint(user_input: str = Form(...)):
    try:
        workflow = WorkflowService.get_workflow("api_creation")
        response = await workflow.execute(user_input)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/healthcheck/postgresql")
async def postgresql_healthcheck(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "detail": str(e)}
    finally:
        db.close()


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
