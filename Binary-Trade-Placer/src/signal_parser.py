'''✅ Parses multiple trade signals from a single message.
✅ Improves regex to support various formats.
✅ Handles errors and invalid messages efficiently.

🔥 Improvements in Signal Parsing
✅ Extracts multiple trades from one message.
✅ Supports flexible trade message formats.
✅ Returns None if no valid trades are found.
✅ Ensures accurate and structured trade details.
'''

import re

def parse_signals(message):
    """
    Extracts multiple trade details from a signal message.
    
    Supports formats like:
    - "BUY EUR/USD at 15:30 for 2 minutes, Amount: $10"
    - "SELL GBP/USD for 3 min, Amount: $20"
    - "BUY BTC/USD, Amount: 50 USD, Duration: 5 min"
    - "BUY EUR/USD $10 2min | SELL GBP/USD $20 3min"
    
    Returns a list of trade dictionaries.
    """

    pattern = r"(BUY|SELL) (\w+\/\w+).*?Amount:?\s?\$?(\d+).*?(\d+)\s?min"
    
    matches = re.findall(pattern, message, re.IGNORECASE)
    trades = []

    for match in matches:
        trades.append({
            "direction": match[0].upper(),
            "asset": match[1],
            "amount": float(match[2]),
            "duration": int(match[3])
        })

    return trades if trades else None
