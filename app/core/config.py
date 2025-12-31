from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_env: str
    debug: bool

    frontend_url: str
    backend_url: str

    enable_credit_reporting: bool
    enable_payments: bool
    enable_notifications: bool

    jwt_issuer: str
    jwt_audience: str

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
