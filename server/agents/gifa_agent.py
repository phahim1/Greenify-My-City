#server/agents/gifa_agent.py


class GIFA:
    def __init__(self):
        self.name = "GIFA"

    def run(self, shared_state: dict) -> dict:
        if shared_state["geji_score"] >= 0.75:
            signal = "Eligible for full green fund allocation"
        else:
            signal = "Recommend co-funding with local government"

        shared_state["investment_signals"].append(signal)
        shared_state["agent_logs"].append(
            f"{self.name}: Investment advice set as: {signal}"
        )
        return shared_state
