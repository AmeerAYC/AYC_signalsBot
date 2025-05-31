import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_signal_to_telegram(signal):
    message = f'''
🚨 توصية جديدة من AYC 🚨

📈 الزوج: {signal["pair"]}
🎯 الدخول: {signal["entry"]}
🎯 الهدف: {signal["tp"]}
❌ الستوب: {signal["sl"]}

📊 {signal["note"]}
    '''
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"})
