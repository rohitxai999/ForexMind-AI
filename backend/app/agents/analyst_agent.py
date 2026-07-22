from app.services.llm_service import LLMService


class AnalystAgent:

    def __init__(self):
        self.llm = LLMService()

    def analyze(self, market_data, news_data):

        prompt = f"""
You are an expert Forex trading analyst.

Market Data:
{market_data}

News:
{news_data}

Analyze the market and return:

1. Signal (BUY, SELL or HOLD)
2. Confidence (0-100)
3. Risk (Low, Medium, High)
4. Short explanation.
"""

        return self.llm.generate(prompt)