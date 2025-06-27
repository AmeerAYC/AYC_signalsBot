from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from analysis import analyze_coin
from halal_filter import is_halal

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ أرسل رمز العملة بعد الأمر. مثال: /analyze BTC")
        return

    symbol = context.args[0].upper()
    
    # تحقق من الحلال
    if not is_halal(symbol):
        await update.message.reply_text(f"⚠️ عملة {symbol} غير موجودة في قائمة العملات الحلال.")
        return

    # تحليل العملة
    analysis_result = analyze_coin(symbol)
    await update.message.reply_text(analysis_result)

if __name__ == '__main__':
    import config
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("analyze", analyze))
    app.run_polling()
