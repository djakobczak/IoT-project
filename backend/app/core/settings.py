from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PORT: int = Field(..., env="BACKEND_PORT")
    HOST: str = Field(..., env="BACKEND_HOST")
    OPERATOR_USERNAME: str
    OPERATOR_PASSWORD: str
    RASPBERRY_PI_USERNAME: str
    RASPBERRY_PI_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
