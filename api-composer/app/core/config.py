from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import dotenv_values

config = dotenv_values(".env")


class Settings(BaseSettings):
    PROJECT_NAME: str = Field(config.get("PROJECT_NAME"))
    VERSION: str = Field(config.get("VERSION"))
    HOST: str = Field(config.get("HOST"))
    PORT: int = Field(config.get("PORT"))
    OPENAI_API_KEY: str = Field(config.get("OPENAI_API_KEY"))
    DB_TYPE: str = Field(config.get("DB_TYPE"))
    DB_USERNAME: str = Field(config.get("DB_USERNAME"))
    DB_PASSWORD: str = Field(config.get("DB_PASSWORD"))
    DB_HOST: str = Field(config.get("DB_HOST"))
    DB_NAME: str = Field(config.get("DB_NAME"))
    MONGO_URI: str = Field(config.get("MONGO_URI"))
    SQLALCHEMY_DATABASE_URL: str = Field(config.get("SQLALCHEMY_DATABASE_URL"))
    RELOAD: bool = Field(config.get("RELOAD"))


settings = Settings()
