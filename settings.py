from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    DB_DRIVER: str = 'postgresql+asyncpg'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'password'
    DB_HOST: str = 'postgres'
    DB_PORT: int = 5432
    DB_NAME: str = 'postgres'

    @property
    def db_url(self) -> str:
        return (
            f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )
