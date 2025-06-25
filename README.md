# 🌿 Greenify My City – AI-Powered Urban Energy Strategy Simulator

⚡️ A multi-agent, AI-assisted tool to simulate sustainable energy strategies for any city using Google Gemini and FastAPI.

---

## 🚀 Overview

**Greenify My City** empowers urban planners, citizens, and policy leaders to explore the impact of energy strategies—tailored by city—on:

- 🌍 CO₂ reduction  
- 💰 Monthly energy cost savings  
- ⚖️ GEJI (Green Energy Justice Index)

It simulates an energy mix and generates a Gemini-powered policy brief from virtual advisors like CLEA, REA, SEA, and more.

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
├── client/ # React frontend (TypeScript)
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
  → Body: `{ "city": "Nairobi", "strategy": "Best CO2" }`  
  → Returns: simulation result object

- `POST /generate-brief`  
  → Body: `{ city, strategy, result }`  
  → Returns: `{ brief: "<markdown string>" }`


---

## 👩‍💻 Multi-Agent Advisory System

At the core of the simulation is a multi-agent engine with the following advisors:

| Agent | Full Name                            | Role Description                                                                  |
|-------|--------------------------------------|-----------------------------------------------------------------------------------|
| CLEA  | City-Level Energy Agent              | Advises on local renewable resource mix based on solar, wind, battery, etc.      |
| REA   | Regional Energy Agent                | Checks alignment with regional or national energy policy and grid readiness.     |
| SEA   | Sustainability & Emissions Agent     | Reviews environmental impact and carbon mitigation potential.                    |
| EPAA  | Energy Poverty Assessment Agent      | Assesses equity, affordability, and access in the proposed strategy.             |
| GTIA  | Global Technology & Innovation Agent | Flags relevant innovations and upcoming technologies.                            |
| GEMA  | Global Energy Market Agent           | Warns about global pricing, import risks, or market opportunities.               |
| GIFA  | Global Investment Fund Agent         | Recommends green funding sources or incentives for implementation.               |
| UIA   | User Interaction Agent               | Highlights how local citizens can participate or contribute to the transition.   |

Each agent provides **structured advice**, which is aggregated into a single Gemini-generated markdown brief.

--- 

##🧾 .env Setup
Create a .env file inside the server/ folder:
GOOGLE_API_KEY=your_actual_gemini_api_key

---

## 🖼️ Screenshots

### Home
![Home Screenshot](https://github.com/phahim1/Greenify-My-City/blob/main/assets/001.jpg)


### City Selection
![City](https://github.com/phahim1/Greenify-My-City/blob/main/assets/002.jpg)

### Generated Policy Brief
![Policy Brief 1](https://github.com/phahim1/Greenify-My-City/blob/main/assets/003.jpg)
![Policy Brief 2](https://github.com/phahim1/Greenify-My-City/blob/main/assets/004.jpg)

---

## 📄 Sample Output

[📥 Download Sample Gemini Policy Brief (PDF)](https://github.com/phahim1/Greenify-My-City/blob/main/assets/Policy.pdf)


---

## 📦 Install & Run
1. Backend (FastAPI)

cd server
pip install -r requirements.txt
uvicorn main:app --reload


---

2. Frontend (React)
cd client
npm install
npm start

---

## 🔮 Future Enhancements
✅ Migrate to Google ADK to use real agent classes with state, scoring, and cooperation

✅ GEJI Scoring Enhancements using equity, affordability, and resilience metrics

✅ Save and retrieve briefs via Firebase or GCP Datastore

✅ Auto-deploy via Cloud Run / Render

🔜 Blockchain Audit Layer: Record strategy decisions and energy performance metrics on-chain

🔜 Multi-Criteria Decision Analysis (MCDA): Let users weigh cost, equity, resilience

🔜 Nash Equilibrium-Based Strategy Optimization

🔜 City-as-a-PED Simulation (Positive Energy Districts)

🔜 Gamified Citizen Engagement Loop

---

##📄 License
MIT License – Free to use with attribution.
