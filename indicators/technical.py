import talib
import pandas as pd
def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    close = df['close'].astype(float)

    # EMA
    df['EMA20'] = talib.EMA(close, timeperiod=20)
    df['EMA50'] = talib.EMA(close, timeperiod=50)

    # RSI
    df['RSI'] = talib.RSI(close, timeperiod=14)

    # ATR (para medir volatilidad, útil para SL y TP dinámico)
    high = df['high'].astype(float)
    low = df['low'].astype(float)
    df['ATR'] = talib.ATR(high, low, close, timeperiod=14)

    return df
