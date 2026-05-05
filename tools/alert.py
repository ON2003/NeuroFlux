def send_alert(alert_payload: dict):
    # In a real scenario, this would format the alert payload into HTML and send via Resend API
    print("--------------------------------------------------")
    print(f"** ALERT TRIGGERED: {alert_payload['anomaly_type']} **")
    print(f"Instrument ID: {alert_payload['instrument_id']}")
    print(f"Severity: {alert_payload['severity'].upper()}")
    print(f"Time: {alert_payload['timestamp']}")
    print(f"Description: {alert_payload['description']}")
    print(f"Action: {alert_payload['recommended_action']}")
    print("--------------------------------------------------")
    print("[Alert] Email dispatched successfully (mock).")
