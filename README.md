<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# NeuroFlux UI

This repository is split into:
- `frontend/`: React + Vite UI
- `backend/`: Python backend utilities and pipeline scripts

View your app in AI Studio: https://ai.studio/apps/fd2931fd-a0ca-494a-9e63-c816702324f4

## Run Locally

**Prerequisites:** Node.js

1. `cd frontend`
2. `npm install`
3. Set `GEMINI_API_KEY` in `.env.local`
4. `npm run dev`

## Docker (Production-style)

The Docker image builds static assets with Vite, then serves them through `nginx` on port `8080`.

### Environment variables

- `GEMINI_API_KEY`: required at image build time because Vite injects it during `npm run build`.

Use `.env.example` as the template:

```bash
cp .env.example .env
```

### Build image

```bash
docker build --build-arg GEMINI_API_KEY="$GEMINI_API_KEY" -t neuroflux-ui:local .
```

### Run container

```bash
docker run --rm -p 8080:8080 neuroflux-ui:local
```

Then open `http://localhost:8080`.

### Docker Compose

```bash
docker compose up --build
```
