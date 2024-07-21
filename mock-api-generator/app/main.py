import uvicorn
from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.healthcheck import perform_health_checks


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION
    )
    app.include_router(router)
    @app.on_event("startup")
    async def startup_event():
        await perform_health_checks()
    setup_logging()
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
