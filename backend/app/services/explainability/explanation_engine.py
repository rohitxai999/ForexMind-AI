from typing import List


class ExplanationEngine:
    """
    Generates a human-readable explanation for every trade decision.
    """

    def generate(
        self,
        action: str,
        confidence: int,
        risk: str,
        rsi: float,
        macd_signal: str,
        ema_signal: str,
        news_sentiment: str,
    ) -> str:

        reasons: List[str] = []

        # RSI
        if rsi < 30:
            reasons.append("RSI indicates the market is oversold.")
        elif rsi > 70:
            reasons.append("RSI indicates the market is overbought.")
        else:
            reasons.append("RSI is in the neutral zone.")

        # MACD
        if macd_signal == "BUY":
            reasons.append("MACD shows a bullish crossover.")
        elif macd_signal == "SELL":
            reasons.append("MACD shows a bearish crossover.")

        # EMA
        if ema_signal == "BUY":
            reasons.append("EMA trend is bullish.")
        elif ema_signal == "SELL":
            reasons.append("EMA trend is bearish.")

        # News
        if news_sentiment == "POSITIVE":
            reasons.append("Market news sentiment is positive.")
        elif news_sentiment == "NEGATIVE":
            reasons.append("Market news sentiment is negative.")
        else:
            reasons.append("Market news sentiment is neutral.")

        explanation = (
            f"Trade Decision: {action}\n"
            f"Confidence: {confidence}%\n"
            f"Risk Level: {risk}\n\n"
            "Reasons:\n"
        )

        for i, reason in enumerate(reasons, start=1):
            explanation += f"{i}. {reason}\n"

        return explanation