from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MT5_LOGIN = os.getenv("MT5_LOGIN")
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")
