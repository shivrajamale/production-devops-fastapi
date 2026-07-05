from fastapi import FastAPI

from app.routers import health
from app.routers import version
from app.routers import users

app = FastAPI(
    title="Production DevOps FastAPI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Production DevOps Project 🚀"
    }

app.include_router(health.router)
app.include_router(version.router)
app.include_router(users.router)