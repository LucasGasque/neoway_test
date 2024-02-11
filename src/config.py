from pydantic_settings import BaseSettings, SettingsConfigDict


class __Settings(BaseSettings):
    LOGGERS: list[str] = ["src:INFO"]
    TEST_BASE_PATH: str

    model_config = SettingsConfigDict(env_file=".env")


settings = __Settings()
