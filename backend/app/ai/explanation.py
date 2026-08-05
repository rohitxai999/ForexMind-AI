from typing import Dict, List


class ExplainableAI:
    """
    Explainable AI Engine
    Generates a human-readable explanation
    for Forex trading predictions.
    """

    def generate_report(
        self,
        prediction: str,
        confidence: float,
        indicators: Dict
    ) -> Dict:

        bullish_factors: List[str] = []
        bearish_factors: List[str] = []

        trend = indicators.get("trend", "Neutral")
        rsi = indicators.get("rsi", 50)
        macd = indicators.get("macd", 0)
        volatility = indicators.get("volatility", 1)

        # Trend
        if trend == "Bullish":
            bullish_factors.append(
                "Overall market trend is bullish."
            )
        elif trend == "Bearish":
            bearish_factors.append(
                "Overall market trend is bearish."
            )
        else:
            bullish_factors.append(
                "Market trend is neutral."
            )

        # RSI
        if rsi < 30:
            bullish_factors.append(
                "RSI indicates the market is oversold."
            )
        elif rsi > 70:
            bearish_factors.append(
                "RSI indicates the market is overbought."
            )
        else:
            bullish_factors.append(
                "RSI is in a healthy range."
            )

        # MACD
        if macd > 0:
            bullish_factors.append(
                "MACD momentum is positive."
            )
        else:
            bearish_factors.append(
                "MACD momentum is negative."
            )

        # Volatility
        if volatility > 2:
            bearish_factors.append(
                "High market volatility increases risk."
            )
        else:
            bullish_factors.append(
                "Market volatility is stable."
            )

        return {
            "prediction": prediction,
            "confidence": confidence,
            "bullish_factors": bullish_factors,
            "bearish_factors": bearish_factors,
            "summary": (
                f"The AI recommends {prediction} "
                f"with {confidence:.1f}% confidence."
            )
        }