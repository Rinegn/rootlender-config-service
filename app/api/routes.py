from fastapi import APIRouter
from app.core.config import settings
from app.core.flags import get_feature_flags

router = APIRouter()

@router.get("/config")
def get_config():
    return {
        "app_name": settings.app_name,
        "app_env": settings.app_env,
        "frontend_url": settings.frontend_url,
        "backend_url": settings.backend_url,
    }

@router.get("/flags")
def get_flags():
    return get_feature_flags()
