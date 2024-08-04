from pydantic import BaseModel
from typing import List, Optional, Any

class APIGenerationRequest(BaseModel):
    description: str
    structures: Optional[dict] = None

class APIGenerationResponse(BaseModel):
    api_spec: Any

class APIUploadResponse(BaseModel):
    message: str
    api_id: str
