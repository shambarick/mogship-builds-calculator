from fastapi import APIRouter

from app.api.api_v1.endpoints import builds

api_router = APIRouter()
api_router.include_router(builds.router, prefix="/builds")
