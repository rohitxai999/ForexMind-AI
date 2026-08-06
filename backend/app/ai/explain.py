class ExplainableAI:

    @staticmethod
    def generate_explanation(features, prediction, probability):

        reasons = []

        if features.get("trend") == "Bullish":
            reasons.append("Trend is Bullish")

        if features.get("trend") == "Bearish":
            reasons.append("Trend is Bearish")

        if features.get("rsi", 50) < 30:
            reasons.append("RSI indicates Oversold")

        if features.get("rsi", 50) > 70:
            reasons.append("RSI indicates Overbought")

        if features.get("macd") == "Bullish":
            reasons.append("MACD Bullish Crossover")

        if features.get("macd") == "Bearish":
            reasons.append("MACD Bearish Crossover")

        if features.get("volume") == "High":
            reasons.append("High Trading Volume")

        if features.get("news") == "Positive":
            reasons.append("Positive News Sentiment")

        if features.get("news") == "Negative":
            reasons.append("Negative News Sentiment")

        if not reasons:
            reasons.append("Prediction generated from AI model")

        return {
            "prediction": prediction,
            "confidence": round(probability * 100, 2),
            "reasons": reasons
        }