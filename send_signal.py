import requests
import os
import random

def send_signal():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    # مثال توصية وهمية
    entry_from = round(random.uniform(0.1, 1.0), 4)
    entry_to = round(entry_from + random.uniform(0.01, 0.05), 4)
    target = round(entry_to + random.uniform(0.05, 0.2), 4)
    stop_loss = round(entry_from - random.uniform(0.01, 0.05), 4)

    message = f"""
📈 توصية تداول جديدة

🚀 منطقة الدخول: من {entry_from} إلى {entry_to}
🎯 الهدف: {target}
🛑 وقف الخسارة: {stop_loss}

📊 المؤشرات:
- برايس أكشن ✅
- EMA 9/20/50/200 ✅
- RSI ✅
- فيبوناتشي ✅
- دايفرجنس ✅
- ضخ سيولة ✅
- SMC ✅

نسبة الربح للخسارة: 3:1
"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=payload)

    print("Signal sent!" if response.status_code == 200 else response.text)

if __name__ == "__main__":
    send_signal()
