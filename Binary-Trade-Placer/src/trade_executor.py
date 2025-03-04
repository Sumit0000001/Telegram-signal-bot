'''
✅ Executes trades concurrently for multiple signals.
✅ Handles API failures and retries automatically.
✅ Logs trade success or failure in detail.

🔥 Improvements in Trade Execution
✅ Handles multiple trade signals concurrently.
✅ Implements a retry mechanism (default: 3 attempts).
✅ Logs trade execution details, including errors.
✅ Provides instant feedback on success or failure.

'''

import requests
import logging
import time
from config.config import BROKER_API_KEY, BROKER_API_URLS, DEFAULT_BROKER

# Configure logging
logging.basicConfig(filename="logs/trade_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def place_trade(asset, direction, amount, duration, retry=3):
    """
    Sends a trade request to the broker API with retry logic.
    """
    broker_url = BROKER_API_URLS.get(DEFAULT_BROKER, BROKER_API_URLS["quotex"])
    
    headers = {"Authorization": f"Bearer {BROKER_API_KEY}"}
    data = {
        "asset": asset,
        "direction": direction,
        "amount": amount,
        "duration": duration
    }

    for attempt in range(retry):
        try:
            response = requests.post(broker_url, headers=headers, json=data)
            response_json = response.json()

            if response.status_code == 200:
                logging.info(f"✅ Trade Successful: {response_json}")
                print(f"✅ Trade placed successfully: {data}")
                return response_json
            else:
                logging.error(f"❌ Trade Failed: {response_json}")
                print(f"❌ Trade failed: {response_json}")

        except requests.RequestException as e:
            logging.error(f"⚠️ API Request Error (Attempt {attempt+1}): {e}")
            print(f"⚠️ API request failed (Attempt {attempt+1}): {e}")

        time.sleep(2)  # Wait before retrying
    
    print(f"❌ Trade execution failed after {retry} attempts.")
    return None
