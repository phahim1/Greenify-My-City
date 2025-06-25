#server/gemini_client.py

import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
#load_dotenv()
#genai.configure()

#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load from correct .env path
load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GOOGLE_API_KEY")
print("✅ Loaded Gemini API Key:", api_key)


# Use Gemini 1.5 Flash
#model = genai.GenerativeModel("models/gemini-1.5-flash")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")



def generate_policy_brief(city: str, result: dict, strategy: str) -> str:
    prompt = generate_policy_prompt(city, result, strategy)
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error generating policy brief: {str(e)}"

#def generate_policy_brief(city, result, strategy):
#    return f"Dummy brief for {city} using strategy {strategy} with GEJI Score {result['geji_score']}"

def generate_policy_prompt(city: str, result: dict, strategy: str) -> str:
    return f"""
# 🌍 City Advisory Brief: {city.title()}

You are an AI-based Multi-Agent Advisory Board. Each agent gives a short contribution based on the data and strategy below.

### 🌐 Strategy Chosen: {strategy}

## 🔢 Input Data
- Solar: {result['energy_mix']['solar']}%
- Wind: {result['energy_mix']['wind']}%
- Battery: {result['energy_mix'].get('battery', 0)}%
- Grid: {result['energy_mix'].get('grid', 0)}%
- CO₂ Reduction: {result['co2_reduction']} tons/person/year
- Monthly Savings: ${result['savings_per_month']}
- GEJI Score: {result['geji_score']}

## 🧠 Agent Contributions
“Each insight below comes from one of our expert agents: CLEA, REA, SEA, UIA, EPAA, GEMA, GTIA, GIFA. Use their signals to build a well-reasoned policy brief for the city of {city}, based on the following simulation result…”

1. **CLEA** (City-Level Energy Agent): Comment on optimal local renewable mix.
2. **REA** (Regional Energy Agent): Discuss national-level alignment or risks.
3. **SEA** (Sustainability & Emissions Agent): Review environmental impact.
4. **EPAA** (Energy Poverty Assessment Agent): Assess current and future affordability and access.
5. **GTIA** (Global Technology & Innovation Agent): Highlight relevant innovation trends.
6. **GEMA** (Global Energy Market Agent): Warn of or leverage global pricing impacts.
7. **GIFA** (Global Investment Fund Agent): Recommend funding pathways.
8. **UIA** (User Interaction Agent): Recommend how citizens can engage and contribute.

## ✍️ Deliverables

- One **joint brief** with key messages from agents.
- Emphasize local relevance.
- Use Markdown formatting.
- Include a final section titled “Integrated Policy Actions” (3–5 bullet points).



"""
