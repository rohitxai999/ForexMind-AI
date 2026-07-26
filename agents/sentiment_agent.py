from textblob import TextBlob


class SentimentAgent:
    """
    Performs simple sentiment analysis for a Forex currency pair.
    """

    def __init__(self):
        self.news_database = {
            "EURUSD": [
                "Euro gains after stronger than expected manufacturing data.",
                "US Dollar weakens amid lower Treasury yields.",
                "ECB officials remain optimistic about economic recovery."
            ],
            "GBPUSD": [
                "Pound rises following positive UK employment figures.",
                "Bank of England keeps interest rates unchanged.",
                "Investors remain confident in the UK economy."
            ],
            "USDJPY": [
                "Japanese Yen weakens as Bank of Japan maintains policy.",
                "US Dollar strengthens on positive economic data.",
                "Market volatility remains low in Asian trading."
            ],
            "AUDUSD": [
                "Australian Dollar gains after strong employment report.",
                "Commodity prices support the Australian economy.",
                "Reserve Bank signals stable monetary policy."
            ]
        }

        self.default_news = [
            "Global markets remain cautious ahead of major economic events.",
            "Forex traders monitor central bank policy decisions.",
            "Investors await important inflation data."
        ]

    def analyze(self, pair):
        """
        Analyze sentiment for a specific currency pair.

        Returns:
        {
            "pair": "EURUSD",
            "overall_sentiment": "Positive",
            "average_score": 0.31,
            "articles": [...]
        }
        """

        news = self.news_database.get(pair, self.default_news)

        articles = []
        scores = []

        for article in news:

            polarity = TextBlob(article).sentiment.polarity
            scores.append(polarity)

            if polarity > 0.2:
                sentiment = "Positive"
            elif polarity < -0.2:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            articles.append(
                {
                    "headline": article,
                    "score": round(polarity, 2),
                    "sentiment": sentiment
                }
            )

        average_score = round(sum(scores) / len(scores), 2)

        if average_score > 0.2:
            overall = "Positive"
        elif average_score < -0.2:
            overall = "Negative"
        else:
            overall = "Neutral"

        return {
            "pair": pair,
            "overall_sentiment": overall,
            "average_score": average_score,
            "articles": articles
        }