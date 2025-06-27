halal_list = [
    "BTC", "ETH", "ADA", "SOL", "AVAX", "LINK", "DOT", "XLM", "MATIC", "ATOM",
    "BNB", "INJ", "NEAR", "OP", "ARB", "SEI", "RNDR", "KAS", "GRT", "EGLD"
    # أضف أو عدل حسب قائمة الحلال التي تعتمدها
]

def is_halal(symbol: str) -> bool:
    return symbol.upper() in halal_list
