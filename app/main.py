from fastapi import FastAPI

from app.api.v1.api import api_router

app = FastAPI(title="Acalmo API")

app.include_router(api_router, prefix="/api/v1")


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {"status": "healthy"}
