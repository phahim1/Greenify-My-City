#server/agents/epaa_agent.py

class EPAA:
    def __init__(self):
        self.name = "EPAA"

    def run(self, shared_state: dict) -> dict:
        solar_pct = shared_state["energy_mix"]["solar"]
        affordability = "High" if solar_pct >= 40 else "Moderate"

        shared_state["energy_poverty"] = {
            "affordability": affordability,
            "access_score": round((solar_pct / 100) * 0.8, 2)
        }

        shared_state["savings_per_month"] = round(solar_pct * 0.4, 2)
        shared_state["agent_logs"].append(
            f"{self.name}: Set affordability to {affordability}, estimated monthly savings."
        )
        return shared_state
