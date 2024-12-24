from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    telegram_bot_token: SecretStr
    redis_dsn: SecretStr | None = None

    api_key: SecretStr
    api_url: str = "http://127.0.0.1:8000/api/v1"
