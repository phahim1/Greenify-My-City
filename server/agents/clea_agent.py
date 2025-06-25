#server/agents/clea_agent.py

class CLEA:
    def __init__(self):
        self.name = "CLEA"

    def run(self, shared_state: dict) -> dict:
        city = shared_state["city"]
        strategy = shared_state["strategy"]

        solar_pct = 50 if strategy == "Best CO2" else 35
        wind_pct = 25
        battery_pct = 15
        grid_pct = 10

        shared_state["energy_mix"] = {
            "solar": solar_pct,
            "wind": wind_pct,
            "battery": battery_pct,
            "grid": grid_pct
        }
        shared_state["co2_reduction"] = round((solar_pct + wind_pct) * 0.015, 2)

        shared_state["agent_logs"].append(
            f"{self.name}: Set energy_mix and estimated CO₂ reduction."
        )
        return shared_state
