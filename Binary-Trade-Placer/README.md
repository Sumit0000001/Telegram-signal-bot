🚀 Binary Options Automatic Trade Placer
This bot listens to trade signals from Telegram and automatically places trades using a broker's API.

🔥 Features
✅ Instant Trade Execution – Trades are placed immediately upon receiving a signal.
✅ Handles Multiple Trades – Can process multiple trades from a single message.
✅ Supports Multiple Brokers – Works with Quotex, IQ Option, and more.
✅ Error Handling & Logging – Retries failed trades and logs all activity.
✅ Secure Credentials – Uses .env file for sensitive API keys.

📌 Installation & Setup
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/Sumit0000001/Telegram-signal-bot.git
cd Binary-Trade-Placer

2️⃣ Install Dependencies
pip install -r requirements.txt
Ensure all required Python packages (like dotenv, httpx, etc.) are installed.

3️⃣ Configure Your Bot
Edit .env file: Add your API keys, bot token, and broker credentials.
Check config.py: Ensure all necessary settings are correct.
📡 How It Works
1️⃣ Trade Signal Received – The bot listens for messages in Telegram.
2️⃣ Signal Parsed – Extracts trade details like asset, direction, amount, and duration.
3️⃣ Trade Executed – Places a trade instantly using the broker’s API.
4️⃣ Logs & Error Handling – Retries failed trades and logs all activity.

✅ Checklist to Ensure Your Bot is Ready
✔️ Dependencies Installed
Run: pip install -r requirements.txt
Ensure all required packages are installed.

✔️ Configuration is Correct
Verify .env and config.py contain valid credentials.

✔️ Telegram Bot Token is Set
Create a bot via BotFather.
Update your bot token in .env.

✔️ Signal Handling is Implemented
signal_parser.py correctly extracts trade details.
trade_listener.py properly listens for signals.
trade_executor.py executes trades as expected.

✔️ Run the Bot
Start the bot using:

python Binary-Trade-Placer/src/main.py
Check for any errors in the console.

✔️ Testing
Send a test signal in the Telegram chat.
Verify that the bot responds and places trades correctly.


🎯 Run the Bot

python src/main.py


🔥 What to Do Next?
If it runs successfully, congratulations! 🎉 Your bot is ready.
If you face any errors, share the error message, and we’ll help you debug! 🚀
👨‍💻 Creators:
Sumit Ruhal & Parvesh Jangra