from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Existing app configuration
    app_env: str
    app_name: str
    debug: bool = False

    # Wiring / registry configuration
    service_name: str
    port: int
    service_registry_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
