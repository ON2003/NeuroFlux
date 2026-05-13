import uuid

def detect_anomaly(telemetry_data: dict) -> dict:
    anomaly_detected = False
    severity = "low"
    anomaly_type = ""
    description = ""
    action = ""

    # Rule 1: Status Code > 400
    if telemetry_data.get("status_code", 200) > 400:
        anomaly_detected = True
        severity = "high"
        anomaly_type = "API/Connection Error"
        description = f"Instrument returned status code {telemetry_data['status_code']}."
        action = "Check instrument network connection."
    
    # Rule 2: Temperature threshold (e.g. > 80C)
    elif telemetry_data.get("temperature", 0) > 80.0:
        anomaly_detected = True
        severity = "critical"
        anomaly_type = "Overheating"
        description = f"Temperature reading {telemetry_data['temperature']}C exceeds safe limit of 80C."
        action = "Power down instrument immediately and inspect cooling system."
        
    # Rule 3: Explicit error message
    elif telemetry_data.get("error_message"):
        anomaly_detected = True
        severity = "medium"
        anomaly_type = "Hardware Fault"
        description = f"Error message reported: {telemetry_data['error_message']}."
        action = "Consult manufacturer manual for error code."

    if anomaly_detected:
        return {
            "alert_id": str(uuid.uuid4()),
            "instrument_id": telemetry_data["instrument_id"],
            "timestamp": telemetry_data["timestamp"],
            "severity": severity,
            "anomaly_type": anomaly_type,
            "description": description,
            "recommended_action": action
        }
    return None
