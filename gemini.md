# Project Constitution

## Data Schemas

### Input Schema (Instrument Telemetry/Logs)
```json
{
  "instrument_id": "string",
  "timestamp": "iso8601",
  "status_code": "integer",
  "temperature": "float",
  "pressure": "float",
  "event_type": "usage | error | telemetry",
  "error_message": "string | null"
}
```

### Output Schema (Alert Payload)
```json
{
  "alert_id": "uuid",
  "instrument_id": "string",
  "timestamp": "iso8601",
  "risk_level": "low | medium | high",
  "signal_type": "early_warning | confirmed_fault",
  "confidence_level": "float (0.0 - 1.0)",
  "issue_detected": "string",
  "recommended_action": "string"
}
```

## Behavioral Rules
- **Rule 1**: Act as a calm, precise laboratory reliability assistant. Provide factual, actionable alerts with no alarmist language.
- **Rule 2**: Distinguish between confirmed faults and early warning signals. Avoid over-alerting.
- **Rule 3**: Never invent root causes.
- **Rule 4**: Never suggest actions outside approved SOPs or automatically change instrument settings.
- **Rule 5**: Prioritize reliability and deterministic behavior over speed.

## Architectural Invariants
- **Layer 1: Architecture**: SOPs written in markdown defining inputs, tool logic, and edge cases.
- **Layer 2: Navigation**: Routes data between SOPs and Tools. Does not perform complex tasks.
- **Layer 3: Tools**: Deterministic Python scripts. Atomic and testable.
- **Source of Truth**: Supabase (PostgreSQL). All modules read/write from here.
