from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://admin:yH3!%40qMv@localhost:5432/gymtracker_db"

    class Config:
        env_file = ".env"    # "hey Pydantic, also read from .env file"

settings = Settings()