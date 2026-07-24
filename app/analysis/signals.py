def generate_signal(df):
    """
    Generate AI trading signal from the latest indicator values.
    """

    latest = df.iloc[-1]

    ema20 = latest["EMA20"]
    ema50 = latest["EMA50"]
    ema200 = latest["EMA200"]

    rsi = latest["RSI"]
    macd = latest["MACD"]
    macd_signal = latest["MACD_SIGNAL"]
    adx = latest["ADX"]

    # -------------------------
    # Trend Detection
    # -------------------------

    if ema20 > ema50 > ema200:
        trend = "Bullish"
    elif ema20 < ema50 < ema200:
        trend = "Bearish"
    else:
        trend = "Sideways"

    # -------------------------
    # Buy / Sell / Hold
    # -------------------------

    signal = "HOLD"

    if (
        trend == "Bullish"
        and rsi < 70
        and macd > macd_signal
        and adx > 25
    ):
        signal = "BUY"

    elif (
        trend == "Bearish"
        and rsi > 30
        and macd < macd_signal
        and adx > 25
    ):
        signal = "SELL"

    # -------------------------
    # Confidence Score
    # -------------------------

    confidence = 50

    if trend != "Sideways":
        confidence += 15

    if adx > 25:
        confidence += 15

    if macd > macd_signal and signal == "BUY":
        confidence += 10

    if macd < macd_signal and signal == "SELL":
        confidence += 10

    if 40 <= rsi <= 60:
        confidence += 10

    confidence = min(confidence, 100)

    return {
        "trend": trend,
        "signal": signal,
        "confidence": confidence,
        "rsi": round(float(rsi), 2),
        "adx": round(float(adx), 2),
    }