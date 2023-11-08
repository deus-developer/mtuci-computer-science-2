from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openweathermap_api_key: str = Field(alias='OPENWEATHERMAP_API_KEY')

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
