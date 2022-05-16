"""Main app module to initialize the FastAPI framework."""
from oracle.routers import decrypt
from fastapi import FastAPI

app = FastAPI()
app.include_router(decrypt.router, tags=["decrypt"])


@app.get("/")
def read_root():
    """Default root."""
    return {"message": "bro"}
