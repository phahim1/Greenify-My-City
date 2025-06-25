# server/agent_core/shared_state.py

def initialize_shared_state(city: str, strategy: str) -> dict:
    return {
        "city": city,
        "strategy": strategy,
        "energy_mix": {},
        "co2_reduction": None,
        "savings_per_month": None,
        "geji_score": None,
        "energy_poverty": {},
        "innovation_pathways": [],
        "investment_signals": [],
        "recommended_actions": [],
        "agent_logs": []
    }
