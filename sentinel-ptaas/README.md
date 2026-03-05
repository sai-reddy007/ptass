# Sentinel PTaaS

Production-ready full-stack skeleton for Penetration Testing as a Service.

## Run with Docker
```bash
cp .env.example .env
cd docker
docker compose up --build
```

## API docs
- Backend: http://localhost:8000/docs
- Frontend: http://localhost:3000
- MinIO console: http://localhost:9001

## Seed sample data
```bash
cd backend
PYTHONPATH=. python scripts/seed_data.py
```
