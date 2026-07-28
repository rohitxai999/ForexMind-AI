class ConsensusAgent:

    def get_decision(
        self,
        technical_signal,
        sentiment_signal,
        probability_score,
        confidence_threshold=80
    ):

        technical_signal = technical_signal.upper()
        sentiment_signal = sentiment_signal.upper()

        # Buy
        if (
            technical_signal == "BUY"
            and sentiment_signal == "BUY"
            and probability_score >= confidence_threshold
        ):
            return {
                "decision": "BUY",
                "confidence": probability_score
            }

        # Sell
        if (
            technical_signal == "SELL"
            and sentiment_signal == "SELL"
            and probability_score >= confidence_threshold
        ):
            return {
                "decision": "SELL",
                "confidence": probability_score
            }

        return {
            "decision": "NO TRADE",
            "confidence": probability_score
        }