from pydantic import BaseModel

class APIGenerationRequest(BaseModel):
    prompt: str
    max_tokens: int = 1000

class APIGenerationResponse(BaseModel):
    generated_text: object

