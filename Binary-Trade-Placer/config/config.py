import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram Bot Credentials
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Group/Channel ID

# Broker API Credentials
BROKER_API_KEY = os.getenv("BROKER_API_KEY")  
TRADE_SOURCE = os.getenv("TRADE_SOURCE")  # Source for trade signals (Telegram, Web, etc.)

# Supported Brokers
BROKER_API_URLS = {
    "quotex": "https://api.quotex.com/v1/trade",
    "iq_option": "https://api.iqoption.com/v1/trade"
}

DEFAULT_BROKER = os.getenv("DEFAULT_BROKER", "quotex")  # Default broker
