import os
import requests
import random
import time
import json

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def get_filtered_coins(limit=100):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    coins = response.json()

    halal_coins = {
        'BTC', 'ETH', 'ADA', 'SOL', 'DOT', 'XRP', 'LTC', 'OP', 'ZIL', 'IGU',
        'GALA', 'APT', 'ENS', 'FLUX', 'IMX', 'RENDER', 'A', 'CKB', 'POWR',
        'EGLD', 'SUI', 'WLD', 'AGIX', 'FET', 'GRT', 'ALGO', 'XLM', 'VET',
        'ICP', 'KAS', 'ARB', 'AVAX'
    }

    filtered = []
    for coin in coins:
        if coin['symbol'].upper() in halal_coins and coin['total_volume'] > 1_000_000:
            filtered.append(coin['id'])
            if len(filtered) >= limit:
                break
    return filtered

def get_ohlcv(symbol, days=2):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {"vs_currency": "usd", "days": days, "interval": "hourly"}
    r = requests.get(url, params=params)
    data = r.json()
    if 'prices' not in data:
        raise Exception(f"No price data for {symbol}")
    prices = data['prices']
    volumes = data['total_volumes']
    return prices, volumes

def calculate_rsi(prices, period=14):
    deltas = [prices[i+1][1] - prices[i][1] for i in range(len(prices)-1)]
    gains = [x if x > 0 else 0 for x in deltas]
    losses = [-x if x < 0 else 0 for x in deltas]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    return 100 - (100 / (1 + rs))

def detect_divergence(prices, volumes):
    if len(prices) < 20 or len(volumes) < 20:
        return False
    price_change = prices[-1][1] - prices[-10][1]
    volume_change = volumes[-1][1] - volumes[-10][1]
    return (price_change > 0 and volume_change < 0) or (price_change < 0 and volume_change > 0)

def detect_ema_signal(prices):
    closes = [p[1] for p in prices]
    if len(closes) < 20:
        return False
    ema9 = sum(closes[-9:]) / 9
    ema20 = sum(closes[-20:]) / 20
    return closes[-1] > ema9 > ema20

def in_fibonacci_zone(prices):
    high = max(p[1] for p in prices)
    low = min(p[1] for p in prices)
    current = prices[-1][1]
    zone = low + (high - low) * 0.618
    return abs(current - zone) / current < 0.02

def generate_signal(symbol):
    try:
        prices, volumes = get_ohlcv(symbol)
        price = prices[-1][1]
        rsi = calculate_rsi(prices)
        divergence = detect_divergence(prices, volumes)
        ema = detect_ema_signal(prices)
        fibo = in_fibonacci_zone(prices)
        confirmations = sum([rsi < 30, divergence, ema, fibo])
        if confirmations >= 3:
            sl = price * 0.985
            tp = price * 1.03
            alert = f"""📊 توصية عملة: {symbol.upper()}
💰 الدخول: {price:.4f}$
🎯 الهدف: {tp:.4f}$
🛑 الوقف: {sl:.4f}$
⏱ سكالبينغ (تحقق الهدف اليومي)"""
            return alert
        else:
            return None
    except:
        return None

def send_all_signals():
    coins = get_filtered_coins()
    random.shuffle(coins)
    sent = 0
    for coin in coins:
        if sent >= 15:
            break
        signal = generate_signal(coin)
        if signal:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {"chat_id": CHAT_ID, "text": signal}
            requests.post(url, data=data)
            sent += 1
            time.sleep(2)

if __name__ == "__main__":
    send_all_signals()
