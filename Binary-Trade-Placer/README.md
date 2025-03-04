# 🚀 Binary Options Automatic Trade Placer

This bot listens to trade signals from Telegram and **automatically places trades** using a broker's API.

## 🔥 Features
✅ **Instant Trade Execution** – Trades are placed immediately upon receiving a signal.  
✅ **Handles Multiple Trades** – Can process multiple trades from a single message.  
✅ **Supports Multiple Brokers** – Works with Quotex, IQ Option, and more.  
✅ **Error Handling & Logging** – Retries failed trades and logs all activity.  
✅ **Secure Credentials** – Uses `.env` file for sensitive API keys.  

---

## 📌 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Sumit0000001/Telegram-signal-bot.git
cd Binary-Trade-Placer


📡 How It Works
Trade Signal Received – The bot listens for messages in Telegram.
Signal Parsed – Extracts trade details like asset, direction, amount, and duration.
Trade Executed – Places a trade instantly with broker API.
Logs & Error Handling – Retries failed trades and logs results.


Run the Bot
python src/main.py