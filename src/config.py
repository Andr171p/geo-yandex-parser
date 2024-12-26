import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_DIR: Path = BASE_DIR / ".env"

load_dotenv(ENV_DIR)


class YandexSettings(BaseSettings):
    maps_url: str = os.getenv("YANDEX_MAPS_URL")


class Settings(BaseSettings):
    yandex: YandexSettings = YandexSettings()


settings = Settings()
