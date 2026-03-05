export default function UploadsPage() {
  return (
    <main className="mx-auto mt-20 max-w-2xl rounded-xl bg-slate-900 p-6">
      <h1 className="text-2xl font-bold">Upload PenTest Report</h1>
      <p className="mt-2 text-slate-300">Supports PDF, JSON, CSV, XML. Reports are parsed asynchronously.</p>
      <form className="mt-4 space-y-3">
        <input type="file" className="w-full rounded bg-slate-800 p-2" />
        <button className="rounded bg-cyan-600 px-4 py-2">Upload Report</button>
      </form>
    </main>
  );
}
