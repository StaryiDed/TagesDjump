from functools import lru_cache
from pydantic import BaseSettings


class APPSettings(BaseSettings):
    PROJECT_NAME: str = "TagesDjump"
    DEBUG: bool = True
    ROOT_PATH = ""

    INFO_LOG_FILE = 'app/logs/' + PROJECT_NAME + '_info.log'
    ERROR_LOG_FILE = 'app/logs/' + PROJECT_NAME + '_error.log'

    class Config:
        env_file = ".env"


@lru_cache()
def get_app_settings() -> APPSettings:
    return APPSettings()
