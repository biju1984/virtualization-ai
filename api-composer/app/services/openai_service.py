import openai
from app.core.config import settings
from openai import OpenAI
from fastapi import HTTPException

# Initialize OpenAI with the API key
openai.api_key = settings.OPENAI_API_KEY

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Respond with json output


def generate_api_specification(description: str) -> dict:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate an API specification for the following description: {description}"}
        ],
        max_tokens=10000
    )
    return {"api_specification": completion}


def health_check_service():
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "This is a health check."}
            ],
            max_tokens=10)
        if completion:
            return {"status": "healthy"}
        else:
            raise HTTPException(
                status_code=500, detail="OpenAI is unhealthy:Result is null")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"OpenAI is unhealthy: {str(e)}")
