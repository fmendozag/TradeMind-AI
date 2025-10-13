from services.mt5_services import initialize_mt5, get_historical_data, shutdown_mt5
from src.signal_generator import generate_signals
import MetaTrader5 as mt5

def main():
    try:
        initialize_mt5()

        df = get_historical_data(symbol="EURUSD", timeframe=mt5.TIMEFRAME_M15, days=5)
        print("📊 Historical Data:")
        print(df.head())

        df = generate_signals(df)
        print("📈 Signals Generated:")
        print(df.tail())

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        shutdown_mt5()

if __name__ == "__main__":
    main()
