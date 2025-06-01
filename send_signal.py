import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_signal():
    message = (
        "🚀 توصية تداول سريعة:\n"
        "🔹 منطقة دخول: 50.00 - 51.00\n"
        "🎯 الهدف: 54.00\n"
        "⛔️ وقف الخسارة: 49.00\n"
        "⚠️ تنبيه: حجز أرباح عند كل ارتفاع 1%\n"
    )

    url = (
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        f"?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    )

    response = requests.get(url)
    if response.status_code == 200:
        print("تم إرسال التوصية بنجاح!")
    else:
        print("فشل في إرسال التوصية:", response.text)

if name == "main":
    send_signal()
