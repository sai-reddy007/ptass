export default function LoginPage() {
  return (
    <main className="mx-auto mt-20 max-w-md rounded-xl bg-slate-900 p-6">
      <h1 className="text-2xl font-bold">Login</h1>
      <form className="mt-4 space-y-3">
        <input className="w-full rounded bg-slate-800 p-2" placeholder="Email" />
        <input className="w-full rounded bg-slate-800 p-2" placeholder="Password" type="password" />
        <button className="w-full rounded bg-cyan-600 p-2">Sign In</button>
      </form>
    </main>
  );
}
