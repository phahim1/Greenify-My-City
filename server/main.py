#server/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from server.agent_simulator import simulate_energy_strategy
from server.gemini_client import generate_policy_brief

app = FastAPI()

# --- Middleware: Allow React frontend to call FastAPI ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# --- Models ---
class SimulationRequest(BaseModel):
    city: str
    strategy: str = "default"

class SimulationResult(BaseModel):
    energy_mix: dict
    co2_reduction: float
    savings_per_month: float
    geji_score: float

class PolicyBriefRequest(BaseModel):
    city: str
    strategy: str
    result: SimulationResult

# --- API Endpoints ---

@app.post("/simulate")
def simulate(req: SimulationRequest):
    try:
        result = simulate_energy_strategy(req.city, req.strategy)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-brief")
def generate_brief(data: PolicyBriefRequest):
    try:
        print(f"Received policy brief request: {data.city}, strategy: {data.strategy}")
        brief = generate_policy_brief(data.city, data.result.dict(), data.strategy)
        print("Brief generated successfully")
        return {"brief": brief}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

