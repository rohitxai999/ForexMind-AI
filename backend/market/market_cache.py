"""
ForexMind AI
Day 8

Live Market Cache
"""

from datetime import datetime
from typing import Dict


class MarketCache:
    def __init__(self):
        self.cache: Dict = {}

    def update(self, symbol: str, bid: float, ask: float):
        self.cache[symbol] = {
            "bid": bid,
            "ask": ask,
            "spread": round(ask - bid, 5),
            "timestamp": datetime.utcnow()
        }

    def get(self, symbol: str):
        return self.cache.get(symbol)

    def all(self):
        return self.cache


market_cache = MarketCache()