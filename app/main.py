from fastapi import FastAPI
from app.routers import health
from app.routers import me
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME, 
    version=settings.APP_VERSION
)

app.include_router(health.router)
app.include_router(me.router)