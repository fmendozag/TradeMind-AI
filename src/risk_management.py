def calculate_trade_levels(df, signal, current_price=None, rr_ratio=2.0):
    last = df.iloc[-1]
    atr = last['ATR']

    # Usa current_price si está disponible, sino usa el close
    entry = current_price if current_price is not None else last['close']

    if signal == "BUY":
        stop_loss = entry - atr
        take_profit = entry + atr * rr_ratio
    elif signal == "SELL":
        stop_loss = entry + atr
        take_profit = entry - atr * rr_ratio
    else:
        return None

    return {
        "Entrada": round(float(entry), 5),
        "Stop Loss": round(float(stop_loss), 5),
        "Take Profit": round(float(take_profit), 5),
        "ATR": round(float(atr), 5)
    }


def confirmation_filter(df, signal):
    """
    Filtro adicional para confirmar entradas.
    Ejemplo: Confirmar si la vela actual cierra por encima o debajo de la EMA.
    """
    last = df.iloc[-1]
    if signal == "BUY" and last['close'] > last['EMA20']:
        return True
    if signal == "SELL" and last['close'] < last['EMA20']:
        return True
    return False
