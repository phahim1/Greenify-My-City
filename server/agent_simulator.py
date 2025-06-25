# server/agent_simulator.py


from server.agent_core.shared_state import initialize_shared_state

# Correctly import your custom agent classes from their respective modules
from server.agents.clea_agent import CLEA
from server.agents.rea_agent import REA
from server.agents.sea_agent import SEA
from server.agents.epaa_agent import EPAA
from server.agents.gema_agent import GEMA
from server.agents.gifa_agent import GIFA
from server.agents.gtia_agent import GTIA
from server.agents.uia_agent import UIA

# The following lines are commented out or removed as they are causing the error
# and are not currently used in the simulate_energy_strategy function.
# # Import AgentSimulator from the installed Google ADK library
# # from adk.agent_simulator import AgentSimulator

# # Initialize the simulator with instances of your agent classes
# # Use the names you imported (CLEA, REA, etc.) directly.
# simulator = AgentSimulator(agents=[
#     CLEA(name="CLEA"),
#     REA(name="REA"),
#     SEA(name="SEA"),
#     EPAA(name="EPAA"),
#     GEMA(name="GEMA"),
#     GIFA(name="GIFA"),
#     GTIA(name="GTIA"),
#     UIA(name="UIA"),
# ])


def run_agents(shared_state: dict) -> dict:
    # Iterate through the list of AgentClasses and run each agent
    # The AgentClass list here should correspond to the classes imported above
    for AgentClass in [CLEA, REA, SEA, EPAA, GEMA, GIFA, GTIA, UIA]:
        agent = AgentClass()
        shared_state = agent.run(shared_state)
    return shared_state

def simulate_energy_strategy(city: str, strategy: str) -> dict:
    # Initialize shared state for the simulation
    shared_state = initialize_shared_state(city, strategy)
    # Run the agents with the shared state
    shared_state = run_agents(shared_state)

    # Prepare and return the output for the frontend
    return {
        "energy_mix": shared_state["energy_mix"],
        "co2_reduction": shared_state["co2_reduction"],
        "savings_per_month": shared_state["savings_per_month"],
        "geji_score": shared_state["geji_score"]
    }