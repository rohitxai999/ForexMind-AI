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
        # Collect live market data
        market_data = self.market.collect_market()

        # Run technical analysis
        technicals = self.technical.analyze(market_data)

        results = {}

        for pair, info in technicals.items():

            # Technical trading signal
            technical_signal = info["signal"]["decision"]

            # Currency pair name (e.g. EURUSD)
            pair_name = pair.replace("=X", "")

            # Run sentiment analysis
            sentiment = self.sentiment.analyze(pair_name)

            # Make final trading decision
            final_decision = self.decision.decide(
                technical_signal,
                sentiment
            )

            # Calculate risk
            risk = self.risk.calculate_risk(final_decision)

            # Store results
            results[pair] = {
                "pair": pair_name,
                "technical": info["signal"],
                "sentiment": sentiment,
                "decision": final_decision,
                "risk": risk
            }

        return results