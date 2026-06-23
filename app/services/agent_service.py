from app.models.agent import Agent

class AgentService:

    def get_agents(self):
        return [
            Agent(
                id=1,
                name="Forge Agent"
            )
        ]