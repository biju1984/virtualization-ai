import openai
from app.core.config import settings

def get_openai_response(prompt: str) -> dict:
    openai.api_key = settings.OPENAI_API_KEY
    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error fetching OpenAI response: {e}")
        return None
