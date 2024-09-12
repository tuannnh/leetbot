from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
OPEN_AI_MODEL = os.getenv("OPEN_AI_MODEL", "gpt-4o")

CLAUDE_AI_KEY = os.getenv("CLAUDE_AI_KEY")
CLAUDE_AI_MODEL = os.getenv("CLAUDE_AI_MODEL", "claude-3-5-sonnet-20240620")

CONSOLE_ENABLE = False
BOT = os.getenv("BOT", "claude")  # "gpt" or "claude"
