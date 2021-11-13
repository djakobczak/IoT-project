from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PORT: int = Field(..., env="FRONTEND_PORT")
    HOST: str = Field(..., env="FRONTEND_HOST")
    OPERATOR_USERNAME: str
    OPERATOR_PASSWORD: str
    BACKEND_URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
