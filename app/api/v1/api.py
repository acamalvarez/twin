from fastapi import APIRouter

from app.api.v1.endpoints import twin

api_router = APIRouter()

api_router.include_router(twin.router, prefix="/twin", tags=["Digital Twin"])
