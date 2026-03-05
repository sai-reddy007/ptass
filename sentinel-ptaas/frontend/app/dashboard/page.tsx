import VulnChart from '@/components/VulnChart';

const cards = [
  { title: 'Assets', value: '128' },
  { title: 'Open Vulnerabilities', value: '58' },
  { title: 'Critical Alerts', value: '8' },
  { title: 'Scans Running', value: '12' },
];

export default function DashboardPage() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold">Client Dashboard</h1>
      <div className="mt-6 grid gap-4 md:grid-cols-4">
        {cards.map((card) => (
          <div key={card.title} className="rounded-xl bg-slate-900 p-4 shadow-lg">
            <p className="text-sm text-slate-400">{card.title}</p>
            <p className="text-2xl font-semibold">{card.value}</p>
          </div>
        ))}
      </div>
      <section className="mt-8">
        <VulnChart />
      </section>
      <section className="mt-8 rounded-xl bg-slate-900 p-4">
        <h2 className="text-xl font-semibold">Risk Heatmap (Preview)</h2>
        <div className="mt-4 grid grid-cols-5 gap-2">
          {Array.from({ length: 25 }).map((_, idx) => (
            <div key={idx} className={`h-8 rounded ${idx % 4 === 0 ? 'bg-red-700' : 'bg-emerald-700'}`} />
          ))}
        </div>
      </section>
    </main>
  );
}
