class SentimentAgent:

    def analyze(self, pair):

        sentiments = {
            "EURUSD": "Bullish",
            "GBPUSD": "Bullish",
            "USDJPY": "Bearish"
        }

        return sentiments.get(pair, "Neutral")