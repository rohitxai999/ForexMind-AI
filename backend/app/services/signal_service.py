from app.ai.explanation import ExplainableAI


class SignalService:
    """
    Service responsible for generating
    Forex trading signals.
    """

    def __init__(self):
        self.xai = ExplainableAI()

    def generate_signal(self):

        # Placeholder values
        # Later these will come from your ML model

        prediction = "BUY"

        confidence = 91.5

        indicators = {
            "trend": "Bullish",
            "rsi": 45,
            "macd": 0.82,
            "volatility": 1.3
        }

        report = self.xai.generate_report(
            prediction=prediction,
            confidence=confidence,
            indicators=indicators
        )

        return report