# NeuroFlux

Repository layout:
- `frontend/`: React + Vite UI
- `backend/`: Python FastAPI service and telemetry pipeline helpers

## Docker Audit Result

Previous state was mixed and production-only:
- single frontend-only Docker image served by `nginx`
- no backend service in compose
- no hot reload workflow in containers
- no development bind-mount strategy for fast iteration

This is now split into professional dev and prod Docker workflows.

## Development (Hot Reload)

Default command:

```bash
docker compose up --build
```

This starts:
- frontend dev server (Vite HMR): `http://localhost:3000`
- backend dev API (uvicorn reload): `http://localhost:8000`
- backend API docs: `http://localhost:8000/docs`

### Why this works well for development

- Frontend source is bind-mounted into the container.
- Backend source is bind-mounted into the container.
- `frontend` uses polling-capable Vite watch configuration for Docker environments.
- `backend` uses `uvicorn --reload` for automatic restart on Python file changes.
- `frontend/node_modules` stays container-local via a named volume to avoid host/container dependency conflicts.

## Production Images

Use optimized production builds:

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build
```

Production endpoints:
- frontend: `http://localhost:8080`
- backend: `http://localhost:8000`

## Environment Variables

Copy template:

```bash
cp .env.example .env
```

Important variables:
- `GEMINI_API_KEY`: used by Vite build/define logic
- `FRONTEND_PORT`, `BACKEND_PORT`: dev port mappings
- `CHOKIDAR_USEPOLLING`, `CHOKIDAR_INTERVAL`: frontend watch reliability in Docker
- `FRONTEND_PROD_PORT`, `BACKEND_PROD_PORT`: production port mappings

## Common Commands

Start dev stack:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up --build -d
```

Stop:

```bash
docker compose down
```

Rebuild from scratch:

```bash
docker compose build --no-cache
docker compose up
```

View logs:

```bash
docker compose logs -f frontend
docker compose logs -f backend
```

## Troubleshooting

- If frontend does not live-reload, keep `CHOKIDAR_USEPOLLING=true` in `.env`.
- If dependencies seem stale, rebuild frontend image: `docker compose build frontend`.
- If Docker daemon is unavailable, start Docker Desktop and retry.
- If ports conflict, change `FRONTEND_PORT`/`BACKEND_PORT` in `.env`.
