# Sentinel PTaaS Architecture

Sentinel PTaaS is a modular SaaS platform for penetration testing operations.

## Services
- **Frontend (Next.js/Tailwind/Chart.js):** dashboards, auth pages, report upload UX.
- **Backend (FastAPI):** JWT auth, RBAC, API resources for assets/vulnerabilities/scans/reports/integrations.
- **Worker (Celery + Redis):** async parsing, tool ingestion, scan execution orchestration.
- **Integrations package:** adapter registry for Cobalt Strike, Bugcrowd, HackerOne, Burp, Nmap, Nessus, OpenVAS, OWASP ZAP.
- **Data plane:** PostgreSQL, Redis, MinIO, Elasticsearch.

## Production notes
- Use external object storage credentials and TLS in deployment.
- Replace placeholder integration logic with vendor APIs.
- Add Alembic migrations and CI pipelines before release.
