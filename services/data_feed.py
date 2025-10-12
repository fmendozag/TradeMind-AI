import MetaTrader5 as mt5
import pandas as pd

def connect_mt5():
    if not mt5.initialize():
        raise Exception("MT5 connection failed")
    print("✅ Connected to MT5")

def get_historical_data(symbol="EURUSD", timeframe=mt5.TIMEFRAME_M15, bars=500):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df[['time','open','high','low','close','tick_volume']]
