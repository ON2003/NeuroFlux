# SOP 01: Data Ingestion

## Goal
Ingest raw telemetry data from laboratory instruments, format it to match our internal `Input Schema`, and store it reliably in the database.

## Inputs
- Instrument logs or API payloads containing: ID, timestamp, status code, temperature, pressure, and error messages.

## Logic / Tool
- **Tool**: `tools/ingest_telemetry.py`
- **Process**:
  1. Receive raw data.
  2. Validate against `Input Schema`.
  3. Connect to Supabase via `.env` credentials.
  4. Insert record into `instruments` table.

## Edge Cases
- Invalid JSON: Log failure locally to `.tmp/ingest_errors.log` and drop the payload.
- Database Timeout: Retry 3 times with exponential backoff before failing.
