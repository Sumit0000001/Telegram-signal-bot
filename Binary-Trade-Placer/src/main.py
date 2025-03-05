'''
✅ Runs the Telegram bot efficiently.
✅ Handles continuous execution without crashes.
✅ Improves reliability and performance.

🔥 Improvements in main.py
✅ Ensures the bot runs continuously (none_stop=True).
✅ Removes unnecessary delays (interval=0 for instant response).
✅ Keeps the structure clean and simple.

'''

import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import without 'src'
from trade_listener import bot


from src.trade_listener import bot


if __name__ == "__main__":
    print("🚀 Trade Bot is running...")
    bot.polling(none_stop=True, interval=0)
