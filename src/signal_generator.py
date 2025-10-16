def generate_signal(df):
    last = df.iloc[-1]

    for col in ['EMA20', 'EMA50', 'RSI']:
        if col not in df.columns:
            raise KeyError(f"❌ Error: La columna '{col}' no existe en el DataFrame")

    if last['EMA20'] > last['EMA50'] and last['RSI'] < 70:
        signal = "BUY"
    elif last['EMA20'] < last['EMA50'] and last['RSI'] > 30:
        signal = "SELL"
    else:
        signal = "NO TRADE"

    df.loc[df.index[-1], 'signal'] = signal  # ✅ Agrega la señal a la última fila
    return df
