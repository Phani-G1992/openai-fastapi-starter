from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    openai_api_key: str
    environment: str = "development"
    debug: bool = True

    class Config:
        env_file = ".env"


class ProductionSettings(Settings):
    debug: bool = False
    environment: str = "production"


class StagingSettings(Settings):
    environment: str = "staging"
    debug: bool = False


class DevelopmentSettings(Settings):
    debug: bool = True
    environment: str = "development"


def get_settings():
    env = os.getenv("APP_ENV", "development")
    if env == "production":
        return ProductionSettings(_env_file=".env.production")
    elif env == "staging":
        return StagingSettings(_env_file=".env.staging")
    else:
        return DevelopmentSettings(_env_file=".env.development")


settings = get_settings()
