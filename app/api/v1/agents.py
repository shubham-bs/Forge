from fastapi import APIRouter

from app.models.agent import Agent
from app.services.agent_service import AgentService

router = APIRouter(
    prefix="/api/v1/agents",
    tags=["Agents"]
)

agent_service = AgentService()

@router.get("", response_model=list[Agent])
def get_agents():
    return agent_service.get_agents()