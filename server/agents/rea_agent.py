#server/agetns/rea_agent.py


class REA:
    def __init__(self):
        self.name = "REA"  # Regional Energy Agent

    def run(self, shared_state: dict) -> dict:
        strategy = shared_state["strategy"]

        risk_score = 0.2 if strategy == "Best Cost" else 0.4
        shared_state["agent_logs"].append(f"{self.name}: Assessed regional risk as {risk_score}.")
        shared_state["risks"] = {"regional_alignment_risk": risk_score}

        return shared_state


