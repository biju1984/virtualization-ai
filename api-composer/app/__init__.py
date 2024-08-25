from fastapi import FastAPI
from app.api.endpoints.nlp import router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()
