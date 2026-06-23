from fastapi import FastAPI
from app.models.db_agent import DBAgent
from app.core.database import Base, engine 

from app.api.v1.health import router as health_router
from app.api.v1.agents import router as agents_router
from app.core.config import settings

app = FastAPI(title="Forge")
Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(agents_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Forge ⚒️",
        "environment": settings.environment
    }