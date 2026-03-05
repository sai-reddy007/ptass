export default function ScanPanelPage() {
  return (
    <main className="mx-auto mt-10 max-w-4xl rounded-xl bg-slate-900 p-6">
      <h1 className="text-2xl font-bold">Scan Orchestration Panel</h1>
      <div className="mt-4 grid gap-3 md:grid-cols-3">
        <input className="rounded bg-slate-800 p-2" placeholder="Asset ID" />
        <select className="rounded bg-slate-800 p-2"><option>Nessus</option><option>Nmap</option><option>OWASP ZAP</option></select>
        <input className="rounded bg-slate-800 p-2" placeholder="CRON (optional)" />
      </div>
      <button className="mt-4 rounded bg-cyan-600 px-4 py-2">Trigger Scan</button>
    </main>
  );
}
