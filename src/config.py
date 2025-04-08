import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    JWT_SECRET: str
    ALGORITHM: str
    TOKEN_EXPIRY: int
    REFRESH_EXPIRY: int
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

Config = Settings()
