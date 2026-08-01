"""
ForexMind AI
Day 8

Multi-Timeframe Analysis Agent
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class TimeframeResult:
    timeframe: str
    trend: str
    confidence: int


class MultiTimeframeAgent:
    def __init__(self):
        self.timeframes = ["M5", "M15", "H1", "H4"]

    def analyze(self, technical_data: Dict) -> Dict:
        """
        technical_data example:
        {
            "M5": "BUY",
            "M15": "BUY",
            "H1": "BUY",
            "H4": "HOLD"
        }
        """

        buy = 0
        sell = 0
        hold = 0

        for tf in self.timeframes:
            signal = technical_data.get(tf, "HOLD").upper()

            if signal == "BUY":
                buy += 1
            elif signal == "SELL":
                sell += 1
            else:
                hold += 1

        if buy > sell:
            trend = "Bullish"
            agreement = buy
        elif sell > buy:
            trend = "Bearish"
            agreement = sell
        else:
            trend = "Neutral"
            agreement = hold

        confidence = int((agreement / len(self.timeframes)) * 100)

        return {
            "trend": trend,
            "confidence": confidence,
            "agreement": f"{agreement}/{len(self.timeframes)}",
            "details": technical_data,
        }


multi_timeframe_agent = MultiTimeframeAgent()