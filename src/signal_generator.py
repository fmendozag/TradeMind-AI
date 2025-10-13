def generate_signal(df):
    last = df.iloc[-1]
    if last['EMA20'] > last['EMA50'] and last['RSI'] < 70:
        return "BUY"
    elif last['EMA20'] < last['EMA50'] and last['RSI'] > 30:
        return "SELL"
    else:
        return "NO TRADE"
