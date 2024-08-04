import openai
from app.schemas import APISpecificationCreate
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_api_specification(description: str) -> APISpecificationCreate:
    response = openai.completions.create(
        engine="gpt-4o-mini",
        prompt=f"Generate an API specification for the following description: {description}",
        max_tokens=200
    )
    api_spec = APISpecificationCreate(
        name="Generated API",
        description=description,
        request_structure=response.choices[0].text,
        response_structure=response.choices[0].text
    )
    return api_spec
