import os.path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    model_config = SettingsConfigDict(env_file=f'{BASE_DIR}/.env')

    def get_db_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")


settings = Settings()
db_url = settings.get_db_url()
