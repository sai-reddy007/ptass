const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

export async function getIntegrationStatus(token: string) {
  const res = await fetch(`${API_URL}/integrations/status`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.json();
}
