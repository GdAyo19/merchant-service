from fastapi import FastAPI

from app.config import get_settings
from app.routes.merchants import router as merchants_router
from app.routes.auth import router as auth_router


settings = get_settings()

app = FastAPI(
    title="Merchant Service",
    version="0.1.0",
    debug=settings.debug,
)


app.include_router(merchants_router)
app.include_router(auth_router)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
    }