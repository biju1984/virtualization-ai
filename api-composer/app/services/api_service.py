import json
import yaml
from datetime import datetime
from fastapi import UploadFile, HTTPException
from bson.objectid import ObjectId
from sqlalchemy.orm import Session
from app.models.specification import Specification
from app.models.database import SessionLocal, mongo_db
from app.schemas.api_schemas import APIGenerationRequest
from app.core.config import settings
from openai import OpenAI

# Initialize OpenAI with the API key
client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def process_natural_language(description: str):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate an API specification for the following description: {description}"}
            ],
            max_tokens=10000
        )
        return completion
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")

async def check_openai_health():
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "This is a health check."}
            ],
            max_tokens=10
        )
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI is unhealthy: {str(e)}")

def process_yaml(content: bytes) -> dict:
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse YAML: {str(e)}")

def process_json(content: bytes) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse JSON: {str(e)}")

def save_specification(name: str, description: str, spec_type: str, spec: dict):
    if settings.DB_TYPE == 'postgresql':
        db = SessionLocal()
        try:
            last_spec = db.query(Specification).order_by(Specification.version.desc()).first()
            new_version = (last_spec.version + 1) if last_spec else 1
            new_spec = Specification(
                name=name,
                description=description,
                version=new_version,
                spec_type=spec_type,
                spec=spec
            )
            db.add(new_spec)
            db.commit()
            db.refresh(new_spec)
            return new_spec.id
        finally:
            db.close()
    elif settings.DB_TYPE == 'mongodb':
        collection = mongo_db['specifications']
        spec_doc = {
            "name": name,
            "description": description,
            "version": 1,  # Versioning can be handled differently in MongoDB
            "spec_type": spec_type,
            "spec": spec,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        result = collection.insert_one(spec_doc)
        return str(result.inserted_id)

def get_specification(spec_id: str):
    if settings.DB_TYPE == 'postgresql':
        db = SessionLocal()
        try:
            spec = db.query(Specification).filter(Specification.id == spec_id).first()
            if not spec:
                return None
            return json.loads(spec.spec)
        finally:
            db.close()
    elif settings.DB_TYPE == 'mongodb':
        collection = mongo_db['specifications']
        spec = collection.find_one({"_id": ObjectId(spec_id)})
        if not spec:
            return None
        return spec

async def parse_structures(request_file: UploadFile, response_file: UploadFile):
    try:
        request_content = await request_file.read()
        response_content = await response_file.read()
        request_data = process_json(request_content) if request_file.filename.endswith('.json') else process_yaml(request_content)
        response_data = process_json(response_content) if response_file.filename.endswith('.json') else process_yaml(response_content)
        return {"request": request_data, "response": response_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing files: {str(e)}")

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

