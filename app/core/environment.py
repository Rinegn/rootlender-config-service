from app.core.config import settings

def validate_environment() -> None:
    required_values = {
        "APP_NAME": settings.app_name,
        "APP_ENV": settings.app_env,
        "FRONTEND_URL": settings.frontend_url,
        "BACKEND_URL": settings.backend_url,
        "JWT_ISSUER": settings.jwt_issuer,
        "JWT_AUDIENCE": settings.jwt_audience,
    }

    missing = [key for key, value in required_values.items() if not value]

    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}"
        )
