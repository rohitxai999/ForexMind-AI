"""
ForexMind AI
Day 8

Economic News Agent
"""

from datetime import datetime


class EconomicNewsAgent:

    def __init__(self):
        self.events = [
            {
                "currency": "USD",
                "event": "Non-Farm Payroll (NFP)",
                "impact": "HIGH",
                "minutes_remaining": 15,
            },
            {
                "currency": "EUR",
                "event": "ECB Interest Rate Decision",
                "impact": "HIGH",
                "minutes_remaining": 180,
            },
        ]

    def check_trading_status(self):

        for event in self.events:

            if (
                event["impact"] == "HIGH"
                and event["minutes_remaining"] <= 30
            ):
                return {
                    "trade_allowed": False,
                    "reason": f'{event["event"]} incoming',
                    "event": event,
                }

        return {
            "trade_allowed": True,
            "reason": "No high-impact news soon.",
            "event": None,
        }


economic_news_agent = EconomicNewsAgent()