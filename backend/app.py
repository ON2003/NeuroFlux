import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from tools.alert import send_alert
from tools.detect import detect_anomaly
from tools.ingest import ingest_data


class TelemetryPayload(BaseModel):
    instrument_id: str = Field(..., min_length=1)
    timestamp: str = Field(..., min_length=1)
    status_code: int
    temperature: float
    pressure: float
    event_type: Optional[str] = None
    error_message: Optional[str] = None


app = FastAPI(title="NeuroFlux Backend", version="1.0.0")


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.post("/telemetry")
def telemetry(payload: TelemetryPayload) -> dict:
    try:
        clean = ingest_data(payload.model_dump())
        anomaly = detect_anomaly(clean)
        if anomaly:
            send_alert(anomaly)
        return {
            "ingested": True,
            "anomaly_detected": anomaly is not None,
            "alert": anomaly,
        }
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=int(os.getenv("BACKEND_PORT", "8000")))
