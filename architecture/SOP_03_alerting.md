# SOP 03: Alert Generation

## Goal
Format a detected anomaly into an actionable, concise alert and deliver it to the user.

## Inputs
- Anomaly Event JSON.

## Logic / Tool
- **Tool**: `tools/send_alert.py`
- **Process**:
  1. Map Anomaly Event to the `Output Schema` (Alert Payload).
  2. Format the payload into an HTML email template.
  3. Dispatch via Resend API.

## Edge Cases
- Email API Rate Limiting: Log to `.tmp/email_errors.log`.
- Missing email recipient: Default to the system admin email.
