from fastapi import FastAPI

from app.config.config import APP_NAME
from app.config.config import APP_VERSION
from app.utils.logger import logger

from app.routers import health
from app.routers import version
from app.routers import users

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

logger.info("Production DevOps FastAPI application started")


@app.get("/")
def home():
    return {
        "message": "Welcome to Production DevOps Project 🚀"
    }


app.include_router(health.router)
app.include_router(version.router)
app.include_router(users.router)