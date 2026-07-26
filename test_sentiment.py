from agents.sentiment_agent import SentimentAgent

agent = SentimentAgent()

results = agent.analyze()

for item in results:
    print("-" * 60)
    print(item["headline"])
    print("Sentiment :", item["sentiment"])
    print("Score     :", item["score"])