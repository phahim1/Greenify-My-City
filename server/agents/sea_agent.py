# File: server/agents/sea_agent.py


class SEA:
    def __init__(self):
        self.name = "SEA"

    def run(self, shared_state: dict) -> dict:
        geji = (shared_state["energy_mix"]["solar"] + shared_state["energy_mix"]["wind"]) / 200
        shared_state["geji_score"] = round(min(1.0, geji), 2)
        shared_state["agent_logs"].append(
            f"{self.name}: Calculated GEJI Score as {shared_state['geji_score']}."
        )
        return shared_state
