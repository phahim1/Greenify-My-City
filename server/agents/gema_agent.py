#server/agents/gema_agent.py

class GEMA:
    def __init__(self):
        self.name = "GEMA"

    def run(self, shared_state: dict) -> dict:
        shared_state["recommended_actions"].append(
            "Leverage international green bonds for solar project financing."
        )
        shared_state["agent_logs"].append(
            f"{self.name}: Suggested using global pricing trends to secure funding."
        )
        return shared_state

