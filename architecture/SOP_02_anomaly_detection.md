# SOP 02: Anomaly Detection

## Goal
Evaluate incoming telemetry data to detect potential failure states before they cause unplanned downtime.

## Inputs
- Clean telemetry record from the database (JSON).

## Logic / Tool
- **Tool**: `tools/detect_anomaly.py`
- **Process**:
  1. Check `status_code`. If `> 400`, immediately flag as anomaly.
  2. Check `error_message`. If not null, flag as anomaly.
  3. (Future) Compare `temperature` and `pressure` against historical averages. For MVP, use static thresholds (e.g., Temperature > 80C).

## Edge Cases
- Missing metrics (e.g., pressure is null): Evaluate remaining metrics. Do not fail the pipeline.
