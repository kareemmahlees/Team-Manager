from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    database: str
    port: int
    user: str
    password: str
    host: str


settings = Settings()
