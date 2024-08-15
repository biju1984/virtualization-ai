import uvicorn
from fastapi import FastAPI
from app.api.endpoints.routes import router
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.healthcheck import perform_health_checks
from fastapi.middleware.cors import CORSMiddleware
import debugpy


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api")

    @app.on_event("startup")
    async def startup_event():
        await perform_health_checks()

    setup_logging()
    return app


app = create_app()

if __name__ == "__main__":
    debugpy.listen(("0.0.0.0", 5678))
    print("Debugger is active")
    uvicorn.run(app, host=settings.HOST,
                port=settings.PORT, reload=settings.RELOAD)
