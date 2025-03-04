'''
✅ Runs the Telegram bot efficiently.
✅ Handles continuous execution without crashes.
✅ Improves reliability and performance.

🔥 Improvements in main.py
✅ Ensures the bot runs continuously (none_stop=True).
✅ Removes unnecessary delays (interval=0 for instant response).
✅ Keeps the structure clean and simple.

'''

from src.trade_listener import bot

if __name__ == "__main__":
    print("🚀 Trade Bot is running...")
    bot.polling(none_stop=True, interval=0)
