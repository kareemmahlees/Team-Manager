from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent / "front.env")


class Settings(BaseSettings):
    api_url: str


settings = Settings()
