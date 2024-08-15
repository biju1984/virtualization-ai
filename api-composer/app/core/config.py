from pydantic_settings import BaseSettings
from pydantic import Field, validator
from dotenv import dotenv_values

config = dotenv_values(".env")


class Settings(BaseSettings):
    PROJECT_NAME: str = Field(config.get("PROJECT_NAME", "API Composer"))
    VERSION: str = Field(config.get("VERSION", "1.0"))
    HOST: str = Field(config.get("HOST", "127.0.0.1"))
    PORT: int = Field(config.get("PORT", 8000))
    OPENAI_API_KEY: str = Field(config.get("OPENAI_API_KEY"))
    DB_TYPE: str = Field(config.get("DB_TYPE", "postgresql"))
    DB_USERNAME: str = Field(config.get("DB_USERNAME"))
    DB_PASSWORD: str = Field(config.get("DB_PASSWORD"))
    DB_HOST: str = Field(config.get("DB_HOST"))
    DB_NAME: str = Field(config.get("DB_NAME"))
    MONGO_URI: str = Field(config.get("MONGO_URI"))
    SQLALCHEMY_DATABASE_URL: str = Field(config.get("SQLALCHEMY_DATABASE_URL"))
    RELOAD: bool = Field(config.get("RELOAD", True))

    @validator("OPENAI_API_KEY")
    def validate_api_key(cls, v):
        if not v:
            raise ValueError("OPENAI_API_KEY must be set")
        return v


settings = Settings()
