from fastapi import APIRouter

from api.v1.endpoints import router as endpoint_router

api_router = APIRouter()
api_router.include_router(endpoint_router, prefix="/v1", tags=["endpoint"])
