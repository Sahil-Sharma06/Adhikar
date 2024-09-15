from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str
    JWT_SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
