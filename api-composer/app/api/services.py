from app.models.gpt3 import GPT3
from app.api.schemas import APIGenerationRequest, APIGenerationResponse, APIUploadResponse
from fastapi import UploadFile
import openapi_schema_pydantic as openapi


gpt3 = GPT3()

async def generate_api(request: APIGenerationRequest) -> APIGenerationResponse:
    generated_text = await gpt3.generate_text(request.prompt, request.max_tokens)
    print(generated_text)
    if not generated_text or generated_text == "Error generating text.":
        generated_text = "Error generating text. Please try again."
    return APIGenerationResponse(generated_text=generated_text)

async def process_natural_language(description: str) -> APIGenerationResponse:
    generated_text = await gpt3.generate_text(description, 100)
    return APIGenerationResponse(generated_text=generated_text)

async def parse_structures(request: UploadFile, response: UploadFile) -> APIUploadResponse:
    # Parse the uploaded files
    request_content = await request.read()
    response_content = await response.read()
    # Process and validate the structures
    return APIUploadResponse(status="success", request_structure=request_content, response_structure=response_content)

async def generate_suggestions(request: APIGenerationRequest) -> APIGenerationResponse:
    suggestions = await gpt3.generate_text(request.prompt, 100)
    return APIGenerationResponse(generated_text=suggestions)

async def finalize_api(request: APIGenerationRequest) -> APIGenerationResponse:
    final_spec = await gpt3.generate_text(request.prompt, 200)
    return APIGenerationResponse(generated_text=final_spec)

async def publish_api(api_id: str) -> APIUploadResponse:
    # Implement the logic to publish the API
    return APIUploadResponse(status="success", api_url=f"https://mockapi.com/{api_id}")

async def test_api(api_id: str, request_data: dict):
    # Implement the logic to test the API
    return {"status": "success", "response": "mock_response"}
