from typing import Dict


class DecisionAgent:
    """
    Converts probabilities into a trading decision.
    """

    def make_decision(
        self,
        buy_probability: int,
        sell_probability: int,
        neutral_probability: int,
    ) -> Dict:

        if buy_probability >= 70:
            return {
                "action": "BUY",
                "confidence": buy_probability,
                "risk": "LOW",
            }

        elif sell_probability >= 70:
            return {
                "action": "SELL",
                "confidence": sell_probability,
                "risk": "LOW",
            }

        elif neutral_probability >= 50:
            return {
                "action": "WAIT",
                "confidence": neutral_probability,
                "risk": "MEDIUM",
            }

        return {
            "action": "NO TRADE",
            "confidence": max(
                buy_probability,
                sell_probability,
                neutral_probability,
            ),
            "risk": "HIGH",
        }