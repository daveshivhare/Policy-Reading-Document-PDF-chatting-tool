import os
from dotenv import load_dotenv

print("Current directory:", os.getcwd())  # Add this line

load_dotenv()
print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))

