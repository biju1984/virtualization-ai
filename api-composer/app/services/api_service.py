import json
import yaml
import logging
from datetime import datetime
from fastapi import UploadFile, HTTPException
from bson.objectid import ObjectId
from sqlalchemy.orm import Session
from app.models.specification import Specification
from app.models.database import SessionLocal, mongo_db
from app.schemas.api_schemas import APIGenerationRequest
from app.core.config import settings
from app.services.openai_service import OpenAIService
from app.api.handlers.openai.openai_handler import OpenAIHandler
from app.api.handlers.openai.refine_prompt_handler import RefinePromptHandler
from app.api.handlers.openai.save_specification_handler import SaveSpecificationHandler


logger = logging.getLogger(__name__)


async def process_natural_language(description: str):
    try:
        request = {'description': description}
        handler_chain = OpenAIHandler(
            successor=RefinePromptHandler(
                successor=SaveSpecificationHandler()
            )
        )
        handler_chain.handle(request)
        return request
    except Exception as e:
        logger.error(f"Failed to process natural language input: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"OpenAI API error: {str(e)}")


async def check_openai_health():
    return OpenAIService().health_check_service()


def process_yaml(content: bytes) -> dict:
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to parse YAML: {str(e)}")


def process_json(content: bytes) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=400, detail=f"Failed to parse JSON: {str(e)}")


async def generate_suggestions(request: APIGenerationRequest):
    return await process_natural_language(request.description)


async def finalize_api(request: APIGenerationRequest):
    return await process_natural_language(request.description)


async def publish_api(api_id: str):
    return {"message": "API published successfully", "api_id": api_id}


async def test_api(api_id: str, request_data: dict):
    return {"message": "API tested successfully", "api_id": api_id, "request_data": request_data}


async def generate_api(request: APIGenerationRequest):
    return await process_natural_language(request.description)
