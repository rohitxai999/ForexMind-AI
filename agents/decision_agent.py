class DecisionAgent:
    """
    Combines technical analysis and sentiment analysis
    to generate the final trading decision.
    """

    def decide(self, technical_signal, sentiment):

        # Get the overall sentiment returned by SentimentAgent
        overall_sentiment = sentiment.get("overall_sentiment", "Neutral")

        # Strong BUY
        if technical_signal == "BUY" and overall_sentiment == "Positive":
            return {
                "decision": "BUY",
                "confidence": "High",
                "reason": "Technical indicators and market sentiment are both bullish."
            }

        # Strong SELL
        if technical_signal == "SELL" and overall_sentiment == "Negative":
            return {
                "decision": "SELL",
                "confidence": "High",
                "reason": "Technical indicators and market sentiment are both bearish."
            }

        # Technical BUY but sentiment disagrees
        if technical_signal == "BUY" and overall_sentiment == "Negative":
            return {
                "decision": "HOLD",
                "confidence": "Medium",
                "reason": "Technical indicators suggest BUY, but sentiment is negative."
            }

        # Technical SELL but sentiment disagrees
        if technical_signal == "SELL" and overall_sentiment == "Positive":
            return {
                "decision": "HOLD",
                "confidence": "Medium",
                "reason": "Technical indicators suggest SELL, but sentiment is positive."
            }

        # Neutral case
        return {
            "decision": "HOLD",
            "confidence": "Low",
            "reason": "No strong agreement between technical analysis and sentiment."
        }