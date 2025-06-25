#server/agents/uia_agent.py


class UIA:
    def __init__(self):
        self.name = "UIA"

    def run(self, shared_state: dict) -> dict:
        shared_state["recommended_actions"].append(
            "Launch a public awareness campaign for rooftop solar benefits."
        )
        shared_state["agent_logs"].append(
            f"{self.name}: Suggested public engagement action."
        )
        return shared_state
