from tradingview_login import get_signals
from send_to_telegram import send_signal_to_telegram

if __name__ == "__main__":
    signals = get_signals()
    for signal in signals:
        send_signal_to_telegram(signal)
