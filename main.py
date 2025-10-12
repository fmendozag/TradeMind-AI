from src.data_loader import initialize_mt5, get_historical_data, shutdown_mt5

if __name__ == "__main__":
    try:
        initialize_mt5()
        df = get_historical_data(symbol="EURUSD", days=3)
        print(df.head(10))
    finally:
        shutdown_mt5()