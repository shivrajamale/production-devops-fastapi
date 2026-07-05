from fastapi import APIRouter
from app.config.config import APP_VERSION
from app.config.config import APP_ENV

router = APIRouter()

@router.get("/version")
def version():
    return {
        "version": APP_VERSION,
        "environment": APP_ENV
    }