# src/data_loader.py

import MetaTrader5 as mt5
import pandas as pd
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

MT5_LOGIN = int(os.getenv("MT5_LOGIN"))
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

def initialize_mt5():
    """Initialize connection with MetaTrader 5"""
    if not mt5.initialize():
        raise RuntimeError(f"MT5 initialize() failed: {mt5.last_error()}")

    authorized = mt5.login(MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
    if not authorized:
        raise RuntimeError(f"MT5 login failed: {mt5.last_error()}")
    print("✅ Connected to MetaTrader 5")

def get_historical_data(symbol="EURUSD", timeframe=mt5.TIMEFRAME_M15, days=5):
    """Get historical data from MT5"""
    utc_from = datetime.now() - timedelta(days=days)
    rates = mt5.copy_rates_from(symbol, timeframe, datetime.now(), days * 24 * 4)  # 4 candles/hour for M15

    if rates is None:
        raise RuntimeError(f"Failed to get data for {symbol}: {mt5.last_error()}")

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df[['time', 'open', 'high', 'low', 'close', 'tick_volume']]

    return df

def shutdown_mt5():
    """Shutdown MT5 connection"""
    mt5.shutdown()
