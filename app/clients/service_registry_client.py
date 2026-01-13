import httpx
from app.core.settings import settings


def register_service():
    payload = {
        "service_name": settings.service_name,
        "port": settings.port,
        "environment": settings.app_env,
        "health_url": f"http://127.0.0.1:{settings.port}/health",
    }

    try:
        with httpx.Client(timeout=2.0) as client:
            client.post(
                f"{settings.service_registry_url}/register",
                json=payload
            )
    except Exception:
        # Fail open during Phase B
        pass
