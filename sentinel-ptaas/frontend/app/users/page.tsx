export default function UserManagementPage() {
  return (
    <main className="mx-auto mt-10 max-w-4xl rounded-xl bg-slate-900 p-6">
      <h1 className="text-2xl font-bold">User Management</h1>
      <table className="mt-4 w-full text-left">
        <thead><tr><th>Email</th><th>Role</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>admin@acme.test</td><td>Security Admin</td><td>Active</td></tr>
          <tr><td>dev@acme.test</td><td>Developer</td><td>Active</td></tr>
        </tbody>
      </table>
    </main>
  );
}
