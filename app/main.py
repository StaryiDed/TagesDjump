from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import ping, fibonacci
from app.core.config import get_app_settings
from app.core.logging import CustomizeLogger


def get_app() -> FastAPI:
    app_settings = get_app_settings()
    server = FastAPI(
        title=app_settings.PROJECT_NAME,
        root_path=app_settings.ROOT_PATH,
    )

    server.include_router(ping.router)
    server.include_router(
        fibonacci.router,
        tags=["fibonacci"],
    )

    server.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    server.logger = CustomizeLogger.make_logger()

    return server


app = get_app()
