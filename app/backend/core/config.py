from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / "api.env")


class Settings(BaseSettings):
    database: str
    port: int
    user: str
    password: str
    host: str
    access_token: str


settings = Settings()
