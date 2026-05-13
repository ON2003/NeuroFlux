import os
import json
from datetime import datetime

# Ingestion mock
def ingest_data(payload: dict) -> dict:
    # Validate payload (mock validation)
    required_keys = ["instrument_id", "timestamp", "status_code", "temperature", "pressure"]
    for key in required_keys:
        if key not in payload:
            raise ValueError(f"Missing required key: {key}")
    
    # In a real scenario, this would write to Supabase
    print(f"[Ingest] Successfully ingested data for instrument {payload['instrument_id']}")
    return payload
