"""
Market Summary Engine
ForexMind AI - Day 11
"""


class MarketSummary:
    """
    Generates a summary of the current market conditions.
    """

    def __init__(self):
        pass

    def generate_summary(self, market_data: dict):

        trend = market_data.get("trend", "Unknown")
        momentum = market_data.get("momentum", "Neutral")
        volatility = market_data.get("volatility", "Medium")
        liquidity = market_data.get("liquidity", "Medium")
        news_risk = market_data.get("news_risk", "Low")
        confidence = market_data.get("confidence", 0)

        # AI Recommendation
        if trend == "Bullish" and confidence >= 80:
            recommendation = "BUY"

        elif trend == "Bearish" and confidence >= 80:
            recommendation = "SELL"

        else:
            recommendation = "HOLD"

        return {
            "trend": trend,
            "momentum": momentum,
            "volatility": volatility,
            "liquidity": liquidity,
            "news_risk": news_risk,
            "confidence": confidence,
            "recommendation": recommendation
        }


if __name__ == "__main__":

    market = {
        "trend": "Bullish",
        "momentum": "Strong",
        "volatility": "Medium",
        "liquidity": "High",
        "news_risk": "Low",
        "confidence": 91
    }

    summary = MarketSummary().generate_summary(market)

    print("=" * 60)
    print("ForexMind AI - Market Summary")
    print("=" * 60)

    for key, value in summary.items():
        print(f"{key.title():15}: {value}")