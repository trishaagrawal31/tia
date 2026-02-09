from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost/tia"
    DATABASE_URL_SYNC: str = "postgresql://user:pass@localhost/tia"

    model_config = {"env_file": ".env"}


settings = Settings()
