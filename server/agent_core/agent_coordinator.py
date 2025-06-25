#server/agent_core/agent_coordinator.py

from server.agent_core.shared_state import initialize_shared_state
from server.agents.clea_agent import CLEA
from server.agents.rea_agent import REA
from server.agents.sea_agent import SEA
from server.agents.uia_agent import UIA
from server.agents.epaa_agent import EPAA
from server.agents.gema_agent import GEMA
from server.agents.gtia_agent import GTIA
from server.agents.gifa_agent import GIFA

def run_agents(city: str, strategy: str) -> dict:
    shared_state = initialize_shared_state(city, strategy)

    agent_classes = [CLEA, REA, SEA, UIA, EPAA, GEMA, GTIA, GIFA]

    for AgentClass in agent_classes:
        agent = AgentClass()
        shared_state = agent.run(shared_state)

    return shared_state
