from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.utils.faker_utils import generate_fake_data
from app.models.database import SessionLocal, APISpecification

async def handle_request(project_name: str, api_version: str, endpoint: str, request: Request):
    db = SessionLocal()
    api_spec = get_api_spec_from_db(project_name, api_version, endpoint, db)
    if not api_spec:
        raise HTTPException(status_code=404, detail="API not found")

    request_data = await request.json() if request.method in ["POST", "PUT"] else {}
    response_data = generate_response(api_spec, request_data)
    return JSONResponse(content=response_data)

def get_api_spec_from_db(project_name: str, api_version: str, endpoint: str, db):
    spec = db.query(APISpecification).filter_by(
        project_name=project_name,
        api_version=api_version,
        endpoint=endpoint
    ).first()
    return spec.spec if spec else None

def generate_response(api_spec: dict, request_data: dict) -> dict:
    response = {}
    for field, field_spec in api_spec['fields'].items():
        response[field] = request_data.get(field, generate_fake_data(field_spec['type']))
    return response
