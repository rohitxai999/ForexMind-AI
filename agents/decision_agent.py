class DecisionAgent:

    def decide(
        self,
        technical_signal,
        sentiment
    ):

        if (
            technical_signal == "BUY"
            and sentiment == "Bullish"
        ):
            return "BUY"

        if (
            technical_signal == "SELL"
            and sentiment == "Bearish"
        ):
            return "SELL"

        return "HOLD"