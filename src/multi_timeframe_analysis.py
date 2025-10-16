import time
from datetime import datetime
from services.mt5_services import initialize_mt5, get_historical_data, shutdown_mt5
from indicators.technical import add_indicators
from src.signal_generator import generate_signal
from src.risk_management import calculate_trade_levels, confirmation_filter
from src.multi_timeframe_analysis import analyze_multi_timeframe  # tu módulo nuevo
import MetaTrader5 as mt5

SYMBOL = "XAUUSD+"
TIMEFRAME = mt5.TIMEFRAME_M1  # usamos 1 min para detección rápida

def main():
    try:
        initialize_mt5()
        print("✅ Conectado a MetaTrader 5. Esperando ticks...")

        last_checked_candle_time = None

        while True:
            tick = mt5.symbol_info_tick(SYMBOL)
            if tick is None:
                print("⚠️ No se pudo obtener el tick.")
                time.sleep(1)
                continue

            df = get_historical_data(symbol=SYMBOL, timeframe=TIMEFRAME, days=1)
            if df is None or df.empty:
                print("⚠️ No se pudo obtener datos históricos.")
                time.sleep(1)
                continue

            last_candle_time = df.iloc[-1]['time']
            if last_checked_candle_time == last_candle_time:
                time.sleep(1)
                continue

            last_checked_candle_time = last_candle_time
            print(f"\n🕒 Nueva vela detectada: {last_candle_time}")

            # Aquí haces análisis multi-timeframe con tu módulo nuevo
            signal, levels = analyze_multi_timeframe(SYMBOL)

            print(f"🧾 Último cierre (M1): {df.iloc[-1]['close']}")
            print(f"🎯 Precio actual: Bid={tick.bid}, Ask={tick.ask}")
            print(f"📊 Señal generada (MTF): {signal}")

            if signal != "NO TRADE":
                if levels:
                    print(f"✅ Entrada confirmada (MTF): {levels}")
                else:
                    print("⚠️ Señal detectada pero sin confirmación final (MTF)")
            else:
                print("❌ No hay señal operable (MTF)")

            time.sleep(1)

    except KeyboardInterrupt:
        print("⏹️ Proceso detenido por el usuario.")

    except Exception as e:
        print(f"❌ Error inesperado: {e}")

    finally:
        shutdown_mt5()
        print("🛑 MetaTrader 5 cerrado.")

if __name__ == "__main__":
    main()

