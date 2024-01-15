from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str

    model_config = SettingsConfigDict(env_file="../../.env")


@lru_cache
def get_settings():
    return Settings()


settings_env = get_settings()
# print(settings_env.NAME)
# print(settings_env.USER)
# print(settings_env.PORT)