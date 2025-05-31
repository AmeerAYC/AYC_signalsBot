from tradingview_login import login_to_tradingview
from send_to_telegram import send_signal_to_telegram
import time

def get_signals():
    # محاكاة لاستخراج توصية – عدل هذه حسب السكربت الحقيقي لاحقًا
    signal = {
        "pair": "BTC/USDT",
        "entry": 67800,
        "target": 69200,
        "stop_loss": 66900,
        "analysis_summary": "توصية احترافية جمعت بين عدة مدارس تحليل فني لتعزيز فرص النجاح."
    }
    return signal

def run_bot():
    print("🚀 بدأ البوت...")
    session = login_to_tradingview()
    
    if session:
        signal = get_signals()
        message = f"""
📊 توصية AYC الحصرية

زوج العملة: {signal['pair']}
🔹 دخول: {signal['entry']}
🎯 هدف: {signal['target']}
⛔️ ستوب: {signal['stop_loss']}

📈 {signal['analysis_summary']}
"""
        send_signal_to_telegram(message)
        print("✅ تم إرسال التوصية.")
    else:
        print("❌ فشل تسجيل الدخول إلى TradingView")

if name == "main":
    while True:
        run_bot()
        time.sleep(900)  # كل 15 دقيقة (900 ثانية)
