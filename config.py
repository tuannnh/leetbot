from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

console_enable=False
