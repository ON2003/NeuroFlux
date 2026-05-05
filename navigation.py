import json
import sys
from datetime import datetime

# Add the tools directory to the python path so we can import them
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))

from ingest import ingest_data
from detect import detect_anomaly
from alert import send_alert

def main():
    print("Initializing NeuroFlux Navigation Layer...")
    
    # 1. Mock incoming telemetry data
    import datetime as dt
    mock_telemetry = {
        "instrument_id": "CENTRIFUGE-001",
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "status_code": 200,
        "temperature": 85.5,  # This should trigger the overheating rule
        "pressure": 1.2,
        "error_message": None
    }
    
    print("\n--- Phase 1: Ingestion ---")
    try:
        clean_data = ingest_data(mock_telemetry)
    except Exception as e:
        print(f"Ingestion failed: {e}")
        return
        
    print("\n--- Phase 2: Anomaly Detection ---")
    anomaly = detect_anomaly(clean_data)
    
    if anomaly:
        print("Anomaly detected! Routing to Alert Generation...")
        print("\n--- Phase 3: Alert Generation ---")
        send_alert(anomaly)
    else:
        print("No anomaly detected. System operating normally.")

if __name__ == "__main__":
    main()
