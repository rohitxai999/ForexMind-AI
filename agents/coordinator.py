from agents.market_agent import MarketAgent
from agents.technical_agent import TechnicalAgent


class Coordinator:

    def __init__(self):
        self.market = MarketAgent()
        self.tech = TechnicalAgent()

    def run(self):

        market = self.market.collect_market()

        analysis = self.tech.analyze(market)

        return analysis