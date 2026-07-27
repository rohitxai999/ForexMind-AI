from agents.base_agent import BaseAgent


class StrategyAgent(BaseAgent):

    def __init__(self):
        super().__init__("Strategy Agent")


    def analyze(self, data):

        technical = data.get(
            "technical_score",
            0
        )

        prediction = data.get(
            "prediction",
            0
        )


        score = technical + prediction


        if score > 0:
            signal = "BUY"

        elif score < 0:
            signal = "SELL"

        else:
            signal = "HOLD"


        confidence = min(
            abs(score) * 30,
            100
        )


        return {

            "agent": self.name,

            "signal": signal,

            "confidence": round(
                confidence,
                2
            ),

            "reason":
            "Based on combined technical and prediction strategy"

        }