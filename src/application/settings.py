from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_endoding = "utf-8"
        env_prefix = "app_"

    MONGODB_URL: str
    MONGODB_NAME: str


settings = AppSettings()  # type: ignore[call-arg]
