// File: client/src/App.tsx

import React, { useState } from "react";
import "./App.css";
import ReactMarkdown from "react-markdown";
import EnergyChart from "./EnergyChart";
import CityAutocomplete from "./CityAutocomplete";

function App() {
  const [city, setCity] = useState("");
  const [strategy, setStrategy] = useState("Best Cost");
  const [result, setResult] = useState({
    energy_mix: { solar: 58, wind: 22, battery: 15, grid: 5 },
    co2_reduction: 1.3,
    savings_per_month: 16,
    geji_score: 0.75,
  });
  const [brief, setBrief] = useState("");
  const [loading, setLoading] = useState(false);

  const multiAgentIntro = `
## 🧠 Multi-Agent Advisory Board
- **CLEA:** City-Level Energy Agent  
- **REA:** Regional Energy Agent  
- **SEA:** Sustainability & Emissions Agent  
- **EPAA:** Energy Poverty Assessment Agent  
- **GTIA:** Global Technology & Innovation Agent  
- **GEMA:** Global Energy Market Agent  
- **GIFA:** Global Investment Fund Agent  
- **UIA:** User Interaction Agent  
`;

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const simResponse = await fetch("http://127.0.0.1:8000/simulate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city, strategy }),
      });
      const simData = await simResponse.json();
      setResult(simData);

      const briefResponse = await fetch("http://127.0.0.1:8000/generate-brief", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city, strategy, result: simData }),
      });
      const briefData = await briefResponse.json();

      setBrief(multiAgentIntro + briefData.brief);
    } catch (error) {
      console.error("❌ Failed to simulate or fetch brief:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App" style={{ padding: "1rem" }}>
      <h1>🌿 Greenify My City</h1>

      <CityAutocomplete onSelect={setCity} />

      <div style={{ margin: "1rem 0" }}>
        <label htmlFor="strategy">Select Strategy: </label>
        <select
          id="strategy"
          onChange={(e) => setStrategy(e.target.value)}
          value={strategy}
        >
          <option value="Best CO2">🌍 Best CO₂ Mitigation</option>
          <option value="Best Cost">💰 Best Cost Efficiency</option>
          <option value="Balanced">⚖️ Balanced Justice</option>
        </select>
      </div>

      <button onClick={handleSubmit}>Generate Policy Brief</button>

      {loading && <p>Loading...</p>}

      {result && <EnergyChart energyMix={result.energy_mix} />}

      {brief && (
        <div className="brief-container" style={{ marginTop: "2rem", textAlign: "left" }}>
          <h2>📄 Generated Policy Brief</h2>
          <ReactMarkdown>{brief}</ReactMarkdown>

          <div className="metrics-summary" style={{ marginTop: "1.5rem" }}>
            <h3>📊 Summary Metrics</h3>
            <ul style={{ listStyleType: "none", paddingLeft: 0 }}>
              <li><strong>GEJI Score:</strong> {result.geji_score.toFixed(2)}</li>
              <li><strong>Monthly Savings:</strong> ${result.savings_per_month.toFixed(2)}</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
