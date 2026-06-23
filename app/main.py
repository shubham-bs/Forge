'''from fastapi import FastAPI
from fastapi import APIRouter
from app.api.v1.health import router as health_router
from app.api.v1.agents import router as agents_router
from app.services.agent_service import AgentService
from app.core.config import settings

app = FastAPI(title="Forge")
router = APIRouter(
    prefix="/api/v1/agents",
    tags=["Agents"]
)

agent_service = AgentService()

app.include_router(health_router)
app.include_router(agents_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Forge ⚒️",
        "environment": settings.environment
        }
    
@router.get("")
def get_agents():
    return agent_service.get_agents()
    '''
    
from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.api.v1.agents import router as agents_router
from app.core.config import settings

app = FastAPI(title="Forge")

app.include_router(health_router)
app.include_router(agents_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Forge ⚒️",
        "environment": settings.environment
    }