from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Production DevOps Project 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }