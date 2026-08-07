from dotenv import load_dotenv
import os

# Load .env from the project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

MONDAY_API_TOKEN = os.getenv("MONDAY_API_TOKEN")
DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
WORKORDER_BOARD_ID = os.getenv("WORKORDER_BOARD_ID")

