"""
ForexMind AI
Day 8

Portfolio Manager
"""


class PortfolioManager:

    def __init__(self):

        self.balance = 10000.0
        self.open_trades = []
        self.closed_trades = []

    def add_trade(self, trade):

        self.open_trades.append(trade)

    def close_trade(self, trade, profit):

        if trade in self.open_trades:
            self.open_trades.remove(trade)

        trade["profit"] = profit

        self.closed_trades.append(trade)

        self.balance += profit

    def win_rate(self):

        if not self.closed_trades:
            return 0

        wins = len(
            [t for t in self.closed_trades if t["profit"] > 0]
        )

        return round(
            wins / len(self.closed_trades) * 100,
            2,
        )

    def portfolio_summary(self):

        total_profit = sum(
            t["profit"] for t in self.closed_trades
        )

        return {
            "balance": round(self.balance, 2),
            "open_trades": len(self.open_trades),
            "closed_trades": len(self.closed_trades),
            "profit": round(total_profit, 2),
            "win_rate": self.win_rate(),
        }


portfolio_manager = PortfolioManager()