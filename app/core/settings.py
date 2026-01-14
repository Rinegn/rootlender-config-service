from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Existing required fields
    app_name: str = "rootlender-config-service"
    service_name: str = "rootlender-config-service"
    app_env: str = "local"
    environment: str = "local"
    port: int = 8000

    # Service discovery
    service_registry_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()
