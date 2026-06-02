# Configuration placeholder. Populate from env in real app.
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./dev.db"
    redis_url: str = "redis://localhost:6379/0"

settings = Settings()
