from agents.base_agent import BaseAgent


class PredictionAgent(BaseAgent):

    def __init__(self):
        super().__init__("Prediction Agent")


    def analyze(self, data):

        prediction = data.get(
            "prediction",
            0
        )


        if prediction > 0.5:
            signal = "BUY"

        elif prediction < -0.5:
            signal = "SELL"

        else:
            signal = "HOLD"


        confidence = abs(prediction) * 100


        return {

            "agent": self.name,

            "signal": signal,

            "confidence": round(
                confidence,
                2
            ),

            "reason":
            "Based on ML prediction probability"

        }