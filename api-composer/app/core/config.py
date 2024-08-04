from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "API Mockup Tool"
    VERSION: str = "1.0.0"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    DB_TYPE: str = Field(..., env="DB_TYPE")
    DB_USERNAME: str = Field(..., env="DB_USERNAME")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_NAME: str = Field(..., env="DB_NAME")
    MONGO_URI: str = Field(..., env="MONGO_URI")
    SQLALCHEMY_DATABASE_URL: str = Field(..., env="SQLALCHEMY_DATABASE_URL")
    RELOAD: bool = True

    class Config:
        env_file = ".env"

settings = Settings()

