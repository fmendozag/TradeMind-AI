import pandas_ta as ta

def add_indicators(df):
    # Exponential Moving Average 20 y 50
    df['EMA20'] = ta.ema(df['close'], length=20)
    df['EMA50'] = ta.ema(df['close'], length=50)
    
    # RSI
    df['RSI'] = ta.rsi(df['close'], length=14)
    
    return df
