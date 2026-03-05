import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold">Sentinel PTaaS</h1>
      <p className="mt-4 text-slate-300">Production-ready penetration testing as a service platform.</p>
      <div className="mt-6 flex gap-4">
        <Link href="/login" className="rounded bg-cyan-600 px-4 py-2">Login</Link>
        <Link href="/dashboard" className="rounded border border-cyan-500 px-4 py-2">Dashboard</Link>
      </div>
    </main>
  );
}
