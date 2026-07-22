from app.agents.news_agent import NewsAgent

agent = NewsAgent()

result = agent.analyze("EUR/USD")

print(result)