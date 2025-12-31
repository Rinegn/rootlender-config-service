from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.include_router(router)

@app.get("/")
def health():
    return {
        "status": "ok",
        "environment": settings.app_env
    }
