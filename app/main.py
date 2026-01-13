from fastapi import FastAPI
from app.api.health_routes import router as health_router
from app.clients.service_registry_client import register_service

app = FastAPI(title="RootLender Config Service")

app.include_router(health_router)

@app.on_event("startup")
def on_startup():
    register_service()
