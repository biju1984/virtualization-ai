from pydantic import BaseModel
from typing import Optional, Dict, Any

class APIGenerationRequest(BaseModel):
    description: str
    structures: Optional[Dict[str, Any]] = None

class APIGenerationResponse(BaseModel):
    api_spec: Dict[str, Any]

class APIUploadResponse(BaseModel):
    message: str
    api_id: str
