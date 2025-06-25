<<<<<<< HEAD
# 🌿 Greenify My City – AI-Powered Urban Energy Strategy Simulator

> ⚡️ A multi-agent, AI-assisted tool to simulate sustainable energy strategies for any city using Google Gemini and FastAPI.

## 🚀 Overview

**Greenify My City** empowers urban planners, citizens, and policy leaders to explore the impact of energy strategies—tailored by city—on:
- CO₂ reduction
- Monthly energy cost savings
- GEJI (Green Energy Justice Index)

It simulates an energy mix and generates a **Gemini-powered policy brief** from virtual advisors like CLEA, REA, SEA, and more.

---

## 🧠 Features

- 🔁 **Multi-Strategy Simulation**: Choose “Best CO₂”, “Best Cost”, or “Balanced” energy strategies.
- 🧪 **Dynamic Simulation Engine**: Generates city-specific energy mix, CO₂ reduction, and GEJI Score.
- 🧾 **AI-Powered Policy Briefs**: Google Gemini generates detailed advisory reports with markdown formatting.
- 📊 **Data Visualization**: View energy mix via interactive charts.
- 🌍 **City Autocomplete**: Select any global city for tailored results.
- 🧵 **Modular Design**: React frontend + FastAPI backend.

---

## 📂 Project Structure

greenify-my-city/
├── client/ # React frontend (TS)
│ ├── src/
│ │ ├── App.tsx # Main UI
│ │ ├── EnergyChart.tsx
│ │ ├── CityAutocomplete.tsx
│ │ └── ...
├── server/ # FastAPI backend (Python)
│ ├── main.py # API endpoints (/simulate, /generate-brief)
│ ├── agent_simulator.py # Strategy simulation logic
│ ├── gemini_client.py # Gemini integration (Markdown brief)
│ └── .env # Google API key



---

## ⚙️ How It Works

1. **User selects a city + strategy** from the dropdown.
2. FastAPI calls `simulate_energy_strategy(...)` → returns:
   - Energy mix %
   - CO₂ reduction (tons/year)
   - Monthly savings
   - GEJI Score
3. Result is sent to Gemini 1.5 Flash model → generates a **Markdown policy brief**.
4. React renders the brief using `react-markdown`.

---

## 🛠️ Tech Stack

| Layer        | Tooling                                   |
|--------------|-------------------------------------------|
| Frontend     | React (TypeScript), react-markdown        |
| Backend      | FastAPI, Python                           |
| AI Platform  | Google Gemini 1.5 Flash via Generative AI |
| Visualization| Chart.js (Energy Mix)                     |
| Geolocation  | Google Maps Autocomplete (City picker)    |

---

## 🌐 API Endpoints

- `POST /simulate`  
  → Body: `{ "city": "Lahore", "strategy": "Best CO2" }`  
  → Returns: simulation result object

- `POST /generate-brief`  
  → Body: `{ city, strategy, result }`  
  → Returns: `{ brief: "<markdown string>" }`

---

## 🧪 Quick Test with Postman

```json
POST http://localhost:8000/generate-brief
{
  "city": "Karachi",
  "strategy": "Balanced",
  "result": {
    "energy_mix": {
      "solar": 40,
      "wind": 30,
      "battery": 20,
      "grid": 10
    },
    "co2_reduction": 1.4,
    "savings_per_month": 18.0,
    "geji_score": 0.78
  }
}




---

## ⚙️ How It Works

1. **User selects a city + strategy** from the dropdown.
2. FastAPI calls `simulate_energy_strategy(...)` → returns:
   - Energy mix %
   - CO₂ reduction (tons/year)
   - Monthly savings
   - GEJI Score
3. Result is sent to Gemini 1.5 Flash model → generates a **Markdown policy brief**.
4. React renders the brief using `react-markdown`.

---

## 🛠️ Tech Stack

| Layer        | Tooling                                   |
|--------------|-------------------------------------------|
| Frontend     | React (TypeScript), react-markdown        |
| Backend      | FastAPI, Python                           |
| AI Platform  | Google Gemini 1.5 Flash via Generative AI |
| Visualization| Chart.js (Energy Mix)                     |
| Geolocation  | Google Maps Autocomplete (City picker)    |

---

## 🌐 API Endpoints

- `POST /simulate`  
  → Body: `{ "city": "Lahore", "strategy": "Best CO2" }`  
  → Returns: simulation result object

- `POST /generate-brief`  
  → Body: `{ city, strategy, result }`  
  → Returns: `{ brief: "<markdown string>" }`

---

## 🧪 Quick Test with Postman

```json
POST http://localhost:8000/generate-brief
{
  "city": "Karachi",
  "strategy": "Balanced",
  "result": {
    "energy_mix": {
      "solar": 40,
      "wind": 30,
      "battery": 20,
      "grid": 10
    },
    "co2_reduction": 1.4,
    "savings_per_month": 18.0,
    "geji_score": 0.78
  }
}



🧾 .env Setup
Create a .env file in server/:

GOOGLE_API_KEY=your_actual_gemini_api_key



📦 Install & Run
1. Backend (FastAPI)
bash
cd server
pip install -r requirements.txt
uvicorn main:app --reload

2. Frontend (React)
bash
cd client
npm install
npm start


🔮 Future Enhancements
✅ Migrate to Google ADK to use real agent classes with state, scoring, and cooperation
✅ GEJI Scoring Enhancements using more granular metrics like equity, affordability, and resilience
✅ Save and retrieve briefs via Firebase or GCP Datastore
✅ Auto-deploy via Cloud Run / Render
🔜 Blockchain Audit Layer: Record strategy decisions and energy performance metrics on-chain for transparency and trust
🔜 Multi-Criteria Decision Analysis (MCDA): Allow weighting of criteria like cost, equity, resilience in strategy selection
🔜 Nash Equilibrium-Inspired Optimization: Enable agents to find optimal strategies where no one can improve without harming others
🔜 City-as-a-PED Simulation: Model cities as future Positive Energy Districts
🔜 Gamified Citizen Engagement: Integrate a feedback loop where users endorse or modify city strategies




📄 License
MIT License – free to use with attribution.







=======
# Greenify-My-City
>>>>>>> 7b410fab5904c3c814c07f616619aaabb1962488
