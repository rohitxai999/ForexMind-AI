from app.agents.market_agent import MarketAgent
from app.agents.news_agent import NewsAgent
from app.agents.analyst_agent import AnalystAgent


class SupervisorAgent:

    def __init__(self):
        self.market = MarketAgent()
        self.news = NewsAgent()
        self.analyst = AnalystAgent()

    def analyze(self, pair):

        market_result = self.market.analyze(pair)

        news_result = self.news.analyze(pair)

        ai_result = self.analyst.analyze(
            market_result,
            news_result
        )

        return {
            "market": market_result,
            "news": news_result,
            "analysis": ai_result
        }