import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Error: Supabase credentials missing in .env")
    exit(1)

try:
    supabase: Client = create_client(url, key)
    # Perform a simple operation to check connectivity
    # For instance, just checking the auth status or attempting to read a mock table
    # This will fail gracefully if the table doesn't exist, which still proves we can reach the API.
    print("Attempting to connect to Supabase...")
    
    # We attempt to query a hypothetical 'instruments' table
    response = supabase.table("instruments").select("*").limit(1).execute()
    print("Connection successful! Handshake established.")
    print(f"Data returned (if any): {response.data}")

except Exception as e:
    print(f"Connection failed: {str(e)}")
