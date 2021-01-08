from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int = 8080
    es_hosts: str = "localhost:9200"
    es_user: Optional[str]
    es_password: Optional[str]

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()