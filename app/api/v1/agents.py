from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.agent import Agent
from app.services.agent_service import AgentService

from app.models.create_agent import CreateAgentRequest

router = APIRouter(
    prefix="/api/v1/agents",
    tags=["Agents"]
)

agent_service = AgentService()


@router.get("", response_model=list[Agent])
def get_agents(db: Session = Depends(get_db)):
    return agent_service.get_agents(db)

@router.post("", response_model=Agent)
def create_agent(request: CreateAgentRequest, db: Session = Depends(get_db)):
    return agent_service.create_agent(request, db)


