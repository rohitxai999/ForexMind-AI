from database.trade_db import TradeDatabase


class PerformanceAnalytics:

    def __init__(self):
        self.db = TradeDatabase()

    def get_statistics(self):

        trades = self.db.get_all_trades()

        total = len(trades)

        open_trades = 0
        closed_trades = 0
        winning = 0
        losing = 0

        for trade in trades:

            status = trade[8]

            if status == "OPEN":
                open_trades += 1

            elif status == "WIN":
                closed_trades += 1
                winning += 1

            elif status == "LOSS":
                closed_trades += 1
                losing += 1

        win_rate = 0

        if closed_trades > 0:
            win_rate = round((winning / closed_trades) * 100, 2)

        return {
            "Total Trades": total,
            "Open Trades": open_trades,
            "Closed Trades": closed_trades,
            "Winning Trades": winning,
            "Losing Trades": losing,
            "Win Rate": f"{win_rate}%"
        }

    def close(self):
        self.db.close()