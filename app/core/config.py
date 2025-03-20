from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    environment: str = "development"
    app_name: str = "OpenAI FastAPI Service"

    class Config:
        env_file = ".env"

settings = Settings()
