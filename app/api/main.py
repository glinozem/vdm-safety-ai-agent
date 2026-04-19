from fastapi import FastAPI

from app.api.router import api_router
from app.config import settings

app = FastAPI(title=settings.app_name, version=settings.app_version)


@app.get("/")
def root() -> dict[str, str]:
    return {"service": settings.app_name, "status": "ok"}


app.include_router(api_router, prefix="/api/v1")
