//client/src/EnergyChart.tsx


import React from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

interface EnergyMix {
  solar: number;
  wind: number;
  battery: number;
  grid: number;
}

interface Props {
  energyMix: EnergyMix;
}

const EnergyChart: React.FC<Props> = ({ energyMix }) => {
  const data = {
    labels: ["Solar", "Wind", "Battery Storage", "Grid"],
    datasets: [
      {
        label: "Energy Mix (%)",
        data: [
          energyMix.solar,
          energyMix.wind,
          energyMix.battery,
          energyMix.grid,
        ],
        backgroundColor: [
          "#f4d03f", // solar - yellow
          "#58d68d", // wind - green
          "#5dade2", // battery - blue
          "#aab7b8", // grid - gray
        ],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div style={{ width: "400px", margin: "20px auto" }}>
      <h3>Energy Mix Overview</h3>
      <Pie data={data} />
    </div>
  );
};

export default EnergyChart;
