from pydantic_settings import BaseSettings, SettingsConfigDict


class __Settings(BaseSettings):
    TEST_BASE_PATH: str

    model_config = SettingsConfigDict(env_file=".env")


settings = __Settings()
