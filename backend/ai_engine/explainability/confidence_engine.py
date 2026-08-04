"""
Confidence Engine
ForexMind AI - Day 11
"""


class ConfidenceEngine:
    """
    Calculates confidence score for AI trade signals.
    """

    def __init__(self):
        pass

    def calculate_confidence(self, indicators: dict):
        score = 0
        max_score = 7

        # EMA
        if indicators.get("ema_cross", False):
            score += 1

        # MACD
        if indicators.get("macd_bullish", False):
            score += 1

        # RSI
        rsi = indicators.get("rsi")

        if rsi is not None:
            if rsi < 35 or rsi > 70:
                score += 1

        # Support
        if indicators.get("support", False):
            score += 1

        # Resistance
        if indicators.get("resistance", False):
            score += 1

        # Volume
        if indicators.get("volume_high", False):
            score += 1

        # Trend
        if indicators.get("trend") in ["Bullish", "Bearish"]:
            score += 1

        confidence = round((score / max_score) * 100, 2)

        return {
            "score": score,
            "max_score": max_score,
            "confidence": confidence
        }


if __name__ == "__main__":

    indicators = {
        "ema_cross": True,
        "macd_bullish": True,
        "rsi": 31,
        "support": True,
        "resistance": False,
        "volume_high": True,
        "trend": "Bullish"
    }

    engine = ConfidenceEngine()

    result = engine.calculate_confidence(indicators)

    print("=" * 50)
    print("ForexMind AI - Confidence Engine")
    print("=" * 50)
    print(f"Indicator Score : {result['score']}/{result['max_score']}")
    print(f"Confidence      : {result['confidence']}%") 