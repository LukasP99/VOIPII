from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ASTERISK_IP: str
    ASTERISK_PORT: int
    AMI_USERNAME: str
    AMI_PASSWORD: str


C = Settings()
