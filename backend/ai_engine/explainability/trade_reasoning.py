"""
Trade Reasoning Engine
ForexMind AI - Day 11
"""

from ai_engine.explainability.decision_explainer import DecisionExplainer
from ai_engine.explainability.confidence_engine import ConfidenceEngine


class TradeReasoning:

    def __init__(self):
        self.explainer = DecisionExplainer()
        self.confidence_engine = ConfidenceEngine()

    def generate_trade_reasoning(self, signal: str, indicators: dict):

        confidence = self.confidence_engine.calculate_confidence(indicators)

        reasons = self.explainer.generate_reasons(indicators)

        return {
            "signal": signal,
            "confidence": confidence["confidence"],
            "indicator_score": f"{confidence['score']}/{confidence['max_score']}",
            "reasons": reasons
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

    reasoning = TradeReasoning()

    result = reasoning.generate_trade_reasoning(
        signal="BUY",
        indicators=indicators
    )

    print("=" * 60)
    print("ForexMind AI - Trade Reasoning")
    print("=" * 60)

    print(f"Signal           : {result['signal']}")
    print(f"Confidence       : {result['confidence']}%")
    print(f"Indicator Score  : {result['indicator_score']}")

    print("\nReasons:")

    for reason in result["reasons"]:
        print(f"✔ {reason}")