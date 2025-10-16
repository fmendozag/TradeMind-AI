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

def get_historical_data(symbol="XAUUSD+", timeframe=mt5.TIMEFRAME_M1, n_bars=500):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_bars)

    if rates is None or len(rates) == 0:
        raise RuntimeError(f"❌ Error al obtener datos de {symbol}: {mt5.last_error()}")

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df[['time', 'open', 'high', 'low', 'close', 'tick_volume']]


def shutdown_mt5():
    """Shutdown MT5 connection"""
    mt5.shutdown()
