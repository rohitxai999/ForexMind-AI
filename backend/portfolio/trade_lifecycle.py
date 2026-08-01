"""
ForexMind AI
Day 8

Trade Lifecycle Manager
"""

from datetime import datetime


class TradeLifecycle:

    def __init__(self):
        self.trades = []

    def create_trade(self, pair, direction, entry_price):

        trade = {
            "pair": pair,
            "direction": direction,
            "entry_price": entry_price,
            "exit_price": None,
            "status": "OPEN",
            "profit": 0.0,
            "opened_at": datetime.now(),
            "closed_at": None,
        }

        self.trades.append(trade)

        return trade

    def activate_trade(self, trade):
        trade["status"] = "ACTIVE"

    def close_trade(self, trade, exit_price, profit):

        trade["status"] = "CLOSED"

        trade["exit_price"] = exit_price

        trade["profit"] = profit

        trade["closed_at"] = datetime.now()

    def get_all(self):
        return self.trades


trade_lifecycle = TradeLifecycle()