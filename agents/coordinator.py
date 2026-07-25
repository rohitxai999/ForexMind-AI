from agents.market_agent import MarketAgent
from agents.technical_agent import TechnicalAgent
from agents.sentiment_agent import SentimentAgent
from agents.risk_agent import RiskAgent
from agents.decision_agent import DecisionAgent


class Coordinator:

    def __init__(self):

        self.market = MarketAgent()
        self.technical = TechnicalAgent()
        self.sentiment = SentimentAgent()
        self.risk = RiskAgent()
        self.decision = DecisionAgent()

    def run(self):

        market_data = self.market.collect_market()

        technicals = self.technical.analyze(market_data)

        results = {}

        for pair, info in technicals.items():

            technical_signal = info["signal"]["decision"]

            sentiment = self.sentiment.analyze(
                pair.replace("=X", "")
            )

            final_decision = self.decision.decide(
                technical_signal,
                sentiment
            )

            risk = self.risk.calculate_risk(
                final_decision
            )

            results[pair] = {
                "technical": info["signal"],
                "sentiment": sentiment,
                "decision": final_decision,
                "risk": risk
            }

        return results