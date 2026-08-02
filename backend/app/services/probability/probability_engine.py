from typing import Dict


class ProbabilityEngine:
    """
    Calculates BUY / SELL / NEUTRAL probabilities
    from technical indicator scores.
    """

    def calculate(
        self,
        rsi: float,
        macd_signal: str,
        ema_signal: str,
        news_sentiment: str,
    ) -> Dict:

        buy_score = 0
        sell_score = 0

        # RSI
        if rsi < 30:
            buy_score += 25
        elif rsi > 70:
            sell_score += 25
        else:
            buy_score += 10
            sell_score += 10

        # MACD
        if macd_signal == "BUY":
            buy_score += 25
        elif macd_signal == "SELL":
            sell_score += 25

        # EMA
        if ema_signal == "BUY":
            buy_score += 25
        elif ema_signal == "SELL":
            sell_score += 25

        # News
        if news_sentiment == "POSITIVE":
            buy_score += 25
        elif news_sentiment == "NEGATIVE":
            sell_score += 25

        total = buy_score + sell_score

        if total == 0:
            return {
                "buy_probability": 0,
                "sell_probability": 0,
                "neutral_probability": 100,
            }

        buy_probability = round((buy_score / total) * 100)
        sell_probability = round((sell_score / total) * 100)

        neutral_probability = max(
            0,
            100 - buy_probability - sell_probability
        )

        return {
            "buy_probability": buy_probability,
            "sell_probability": sell_probability,
            "neutral_probability": neutral_probability,
        }