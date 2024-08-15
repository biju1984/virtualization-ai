from app.models.openai_integration import get_openai_response

def handle_prompt(prompt: str) -> dict:
    openai_response = get_openai_response(prompt)
    if not openai_response:
        return {"error": "Failed to get a response from OpenAI"}
    return openai_response
