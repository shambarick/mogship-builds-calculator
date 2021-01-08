from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core import es
from app.core.config import get_settings


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_event_handler("startup", es.connect)
    app.add_event_handler("shutdown", es.close)
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()



if __name__ == "__main__":
    uvicorn.run("main:app", port=get_settings().port)
