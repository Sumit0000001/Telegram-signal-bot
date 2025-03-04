'''
✅ Instant trade execution when a message arrives.
✅ Supports multiple trades in a single message.
✅ Executes trades asynchronously without blocking the bot.

🔥 Improvements in Trade Listener
✅ Processes multiple trades concurrently without delays.
✅ Runs in the background without blocking the bot.
✅ Handles large messages efficiently.
✅ Ensures immediate execution of trades.

'''

import telebot
import logging
import threading
from config.config import TELEGRAM_BOT_TOKEN
from src.signal_parser import parse_signals
from src.trade_executor import place_trade

# Configure logging
logging.basicConfig(filename="logs/trade_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Initialize Telegram Bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def process_trade_signals(trade_signals):
    """
    Process and execute multiple trade signals in separate threads.
    """
    for trade in trade_signals:
        trade_thread = threading.Thread(
            target=place_trade,
            args=(trade["asset"], trade["direction"], trade["amount"], trade["duration"])
        )
        trade_thread.start()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """
    Handles incoming Telegram messages, extracts trade signals, and executes them.
    """
    trade_signals = parse_signals(message.text)
    
    if trade_signals:
        logging.info(f"📩 Trade Signal Received: {trade_signals}")
        process_trade_signals(trade_signals)  # Execute trades concurrently
    else:
        logging.info("⚠️ No valid trade signal found.")

if __name__ == "__main__":
    print("🚀 Trade Listener is running...")
    bot.polling(none_stop=True, interval=0)
