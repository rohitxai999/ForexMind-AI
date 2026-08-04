"""
Decision Explainer Module
ForexMind AI - Day 11
"""


class DecisionExplainer:
    """
    Generates human-readable explanations
    for AI trading decisions.
    """

    def __init__(self):
        pass

    def generate_reasons(self, indicators: dict):
        reasons = []

        # EMA Cross
        if indicators.get("ema_cross", False):
            reasons.append("EMA 50 crossed EMA 200 (Bullish Trend)")

        # MACD
        if indicators.get("macd_bullish", False):
            reasons.append("MACD Bullish Crossover detected")

        # RSI
        rsi = indicators.get("rsi")

        if rsi is not None:
            if rsi < 35:
                reasons.append(f"RSI = {rsi} (Oversold)")
            elif rsi > 70:
                reasons.append(f"RSI = {rsi} (Overbought)")
            else:
                reasons.append(f"RSI = {rsi} (Neutral)")

        # Support
        if indicators.get("support", False):
            reasons.append("Price bounced from a strong support level")

        # Resistance
        if indicators.get("resistance", False):
            reasons.append("Price rejected from resistance")

        # Volume
        if indicators.get("volume_high", False):
            reasons.append("High trading volume confirms momentum")

        # Trend
        trend = indicators.get("trend")

        if trend == "Bullish":
            reasons.append("Overall market trend is Bullish")

        elif trend == "Bearish":
            reasons.append("Overall market trend is Bearish")

        elif trend == "Sideways":
            reasons.append("Market is currently ranging")

        return reasons


if __name__ == "__main__":

    indicators = {
        "ema_cross": True,
        "macd_bullish": True,
        "rsi": 31,
        "support": True,
        "volume_high": True,
        "trend": "Bullish"
    }

    explainer = DecisionExplainer()

    explanations = explainer.generate_reasons(indicators)

    print("=" * 50)
    print("ForexMind AI - Decision Explanation")
    print("=" * 50)

    for reason in explanations:
        print(f"✔ {reason}")