def generate_explanation(result):
    """
    Generate a human-readable explanation for the AI signal.
    """

    trend = result["trend"]
    signal = result["signal"]
    confidence = result["confidence"]
    rsi = result["rsi"]
    adx = result["adx"]

    lines = []

    lines.append(f"Market Trend: {trend}.")
    lines.append(f"Signal: {signal}.")
    lines.append(f"Confidence Score: {confidence}%.")

    if trend == "Bullish":
        lines.append("Short-term moving averages indicate an upward trend.")
    elif trend == "Bearish":
        lines.append("Short-term moving averages indicate a downward trend.")
    else:
        lines.append("The market is currently moving sideways.")

    if rsi > 70:
        lines.append("RSI suggests the market is overbought.")
    elif rsi < 30:
        lines.append("RSI suggests the market is oversold.")
    else:
        lines.append("RSI is in a neutral range.")

    if adx > 25:
        lines.append("ADX indicates a strong trend.")
    else:
        lines.append("ADX indicates a weak trend.")

    return " ".join(lines)