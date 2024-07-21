from fastapi import APIRouter, HTTPException, Request
from app.services.api_service import save_specification, get_specification

router = APIRouter()

@router.post("/save-specification/")
async def save_spec(request: Request):
    data = await request.json()
    spec = data.get("spec")
    version = save_specification(spec)
    return {"version": version}

@router.get("/get-specification/{version}")
async def get_spec(version: int):
    spec = get_specification(version)
    if not spec:
        raise HTTPException(status_code=404, detail="Specification not found")
    return {"spec": spec}
