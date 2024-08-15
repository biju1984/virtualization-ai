import openai
from app.core.config import settings
from openai import OpenAI
from fastapi import HTTPException
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI as LangchainOpenAI

from app.core.config import settings


class OpenAIService:
    def __init__(self, api_key: str = settings.OPENAI_API_KEY):
        self.api_key = api_key
        openai.api_key = api_key
        self.client = openai

    def generate_specification(self, description: str) -> dict:
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Generate an API specification for the following description: {description}"}
                ],
                max_tokens=10000
            )
            return {"api_specification": completion}
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"OpenAI API error: {str(e)}"
            )

    def health_check_service(self) -> dict:
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "This is a health check."}
                ],
                max_tokens=10
            )
            if completion:
                return {"status": "healthy"}
            else:
                raise HTTPException(
                    status_code=500, detail="OpenAI is unhealthy: Result is null"
                )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"OpenAI is unhealthy: {str(e)}"
            )

    def create_openai_chain(self) -> LLMChain:
        template = "You are a helpful assistant. Given the following description, generate an API specification: {description}"
        openai_model = LangchainOpenAI(temperature=0.5)
        prompt = PromptTemplate(
            template=template, input_variables=["description"])

        # Using LangChain's OpenAI integration

        return LLMChain(llm=openai_model, prompt=prompt)
