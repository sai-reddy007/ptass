'use client';

import { ArcElement, CategoryScale, Chart as ChartJS, Legend, LinearScale, LineElement, PointElement, Tooltip } from 'chart.js';
import { Doughnut, Line } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, LineElement, PointElement);

export default function VulnChart() {
  return (
    <div className="grid gap-6 md:grid-cols-2">
      <div className="rounded-xl bg-slate-900 p-4">
        <h3 className="mb-3 font-semibold">Severity Distribution</h3>
        <Doughnut
          data={{
            labels: ['Critical', 'High', 'Medium', 'Low'],
            datasets: [{ data: [8, 17, 25, 14], backgroundColor: ['#dc2626', '#ea580c', '#ca8a04', '#16a34a'] }],
          }}
        />
      </div>
      <div className="rounded-xl bg-slate-900 p-4">
        <h3 className="mb-3 font-semibold">Vulnerability Trend</h3>
        <Line
          data={{
            labels: ['W1', 'W2', 'W3', 'W4'],
            datasets: [{ label: 'Open vulns', data: [77, 72, 63, 58], borderColor: '#22d3ee' }],
          }}
        />
      </div>
    </div>
  );
}
