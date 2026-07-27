from agents.technical_agent import TechnicalAgent
from agents.sentiment_agent import SentimentAgent
from agents.prediction_agent import PredictionAgent
from agents.risk_agent import RiskAgent
from agents.strategy_agent import StrategyAgent
from agents.debate_agent import DebateAgent


class AgentCoordinator:

    def __init__(self):

        self.technical = TechnicalAgent()
        self.sentiment = SentimentAgent()
        self.prediction = PredictionAgent()
        self.risk = RiskAgent()
        self.strategy = StrategyAgent()
        self.debate = DebateAgent()


    def analyze_market(self, market_data):

        agents_output = []


        # Get currency pair
        pair = list(market_data.keys())[0]


        # --------------------
        # Technical Agent
        # --------------------

        technical_result = self.technical.analyze(
            market_data
        )

        agents_output.extend(
            technical_result
        )


        # --------------------
        # Sentiment Agent
        # --------------------

        sentiment_result = self.sentiment.analyze(
            pair
        )

        agents_output.append(
            sentiment_result
        )


        # --------------------
        # Prediction Agent
        # --------------------

        prediction_result = self.prediction.analyze(
            market_data[pair]
        )

        agents_output.append(
            prediction_result
        )


        # --------------------
        # Strategy Agent
        # --------------------

        strategy_result = self.strategy.analyze(
            market_data[pair]
        )

        agents_output.append(
            strategy_result
        )


        # --------------------
        # Debate Agent
        # --------------------

        debate_result = self.debate.analyze(
            agents_output
        )


        # --------------------
        # Risk Agent
        # --------------------

        risk_result = self.risk.calculate_risk(
            debate_result
        )


        return {

            "agents": agents_output,

            "debate": debate_result,

            "risk": risk_result

        }