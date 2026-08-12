from typing import Dict, Optional


class DecisionAgent:
    """
    Converts probabilities and SMC/ICT liquidity context
    into a trading decision.
    """

    def make_decision(
        self,
        buy_probability: int,
        sell_probability: int,
        neutral_probability: int,
        liquidity_bias: Optional[str] = None,
        liquidity_confidence: float = 0.0,
    ) -> Dict:

        adjusted_buy = buy_probability
        adjusted_sell = sell_probability

        if liquidity_bias == "BULLISH":
            adjusted_buy += liquidity_confidence

        elif liquidity_bias == "BEARISH":
            adjusted_sell += liquidity_confidence

        adjusted_buy = min(100, adjusted_buy)
        adjusted_sell = min(100, adjusted_sell)

        if adjusted_buy >= 70:
            return {
                "action": "BUY",
                "confidence": round(adjusted_buy, 2),
                "risk": "LOW",
                "liquidity_bias": liquidity_bias or "NEUTRAL",
            }

        elif adjusted_sell >= 70:
            return {
                "action": "SELL",
                "confidence": round(adjusted_sell, 2),
                "risk": "LOW",
                "liquidity_bias": liquidity_bias or "NEUTRAL",
            }

        elif neutral_probability >= 50:
            return {
                "action": "WAIT",
                "confidence": neutral_probability,
                "risk": "MEDIUM",
                "liquidity_bias": liquidity_bias or "NEUTRAL",
            }

        return {
            "action": "NO TRADE",
            "confidence": max(
                adjusted_buy,
                adjusted_sell,
                neutral_probability,
            ),
            "risk": "HIGH",
            "liquidity_bias": liquidity_bias or "NEUTRAL",
        }
