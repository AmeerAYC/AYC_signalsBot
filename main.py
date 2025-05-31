
import os
import telegram
from flask import Flask, request

app = Flask(__name__)
bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
chat_id = os.environ['CHAT_ID']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'No message provided')
    result = data.get('result', '')
    price_zone = data.get('price_zone', '')
    target = data.get('target', '')
    stop = data.get('stop', '')

    signal_message = f"""📊 توصية جديدة من AYC 📊

🔸 الدخول: {price_zone}
🎯 الهدف: {target}
⛔️ وقف الخسارة: {stop}

🧠 تحليل احترافي دقيق جمع بين أكثر من مدرسة تحليل.
📌 هل ستنجح الصفقة؟ تابع التحديثات...
""" 

    if result == "success":
        signal_message += "\n✅ الصفقة نجحت وحققت الهدف!"
    elif result == "fail":
        signal_message += "\n❌ الصفقة ضربت وقف الخسارة."

    bot.send_message(chat_id=chat_id, text=signal_message)
    return "ok"
