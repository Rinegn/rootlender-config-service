from fastapi import FastAPI

# Core routers
from app.api.health_routes import router as health_router

# Optional service-specific routers
# (Add more imports here as the service grows)
# Example:
# from app.api.dependency_routes import router as dependency_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="RootLender Service",
        version="1.0.0",
    )

    # Health (REQUIRED for wiring)
    app.include_router(health_router)

    # Service-specific routers (uncomment as needed)
    # app.include_router(dependency_router, prefix="/dependencies", tags=["dependencies"])

    return app


app = create_app()
