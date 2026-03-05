export default function IntegrationStatusPage() {
  return (
    <main className="mx-auto mt-10 max-w-4xl rounded-xl bg-slate-900 p-6">
      <h1 className="text-2xl font-bold">Integration Status</h1>
      <ul className="mt-4 space-y-2">
        {['Cobalt Strike', 'Bugcrowd', 'HackerOne', 'Burp Suite', 'Nessus', 'Nmap', 'OpenVAS', 'OWASP ZAP'].map((tool) => (
          <li key={tool} className="rounded bg-slate-800 p-3">{tool}: Connected (stub)</li>
        ))}
      </ul>
    </main>
  );
}
