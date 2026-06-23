from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.models.db_agent import DBAgent

from app.models.create_agent import CreateAgentRequest


class AgentService:

    def get_agents(self, db: Session):
        agents = db.query(DBAgent).all()

        return [
            Agent(
                id= agent.id,
                name= agent.name
            )
            for agent in agents
        ]
        
    def create_agent(self,request: CreateAgentRequest,db: Session):
        db_agent = DBAgent(
        name= request.name
        )

        db.add(db_agent)
        db.commit()
        db.refresh(db_agent)

        return Agent(id= db_agent.id, name= db_agent.name)