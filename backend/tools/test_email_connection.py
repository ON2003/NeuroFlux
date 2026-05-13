import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.environ.get("RESEND_API_KEY")

if not resend.api_key:
    print("Error: Resend API key missing in .env")
    exit(1)

try:
    print("Attempting to send a test email via Resend...")
    params = {
        "from": "NeuroFlux <onboarding@resend.dev>",
        "to": ["delivered@resend.dev"],
        "subject": "NeuroFlux Handshake Test",
        "html": "<strong>It works!</strong><br>The NeuroFlux alerting system has established a connection.",
    }
    
    email = resend.Emails.send(params)
    print("Email sent successfully! Handshake established.")
    print(f"Email ID: {email['id']}")

except Exception as e:
    print(f"Failed to send email: {str(e)}")
