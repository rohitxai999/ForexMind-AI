from typing import Dict, List

from app.trading.models import Trade


class TradeAnalytics:
    """Calculates trading performance metrics for ForexMind AI."""

    def __init__(self, trades: List[Trade]):
        self.trades = trades

    def closed_trades(self) -> List[Trade]:
        return [trade for trade in self.trades if trade.result is not None]

    def total_trades(self) -> int:
        return len(self.closed_trades())

    def winning_trades(self) -> int:
        return sum(1 for trade in self.closed_trades() if trade.result == "WIN")

    def losing_trades(self) -> int:
        return sum(1 for trade in self.closed_trades() if trade.result == "LOSS")

    def breakeven_trades(self) -> int:
        return sum(1 for trade in self.closed_trades() if trade.result == "BREAKEVEN")

    def win_rate(self) -> float:
        total = self.total_trades()
        if total == 0:
            return 0.0
        return round((self.winning_trades() / total) * 100, 2)

    def total_profit(self) -> float:
        return round(
            sum(trade.pnl for trade in self.closed_trades() if trade.pnl > 0),
            2,
        )

    def total_loss(self) -> float:
        return round(
            sum(trade.pnl for trade in self.closed_trades() if trade.pnl < 0),
            2,
        )

    def net_pnl(self) -> float:
        return round(
            sum(trade.pnl for trade in self.closed_trades()),
            2,
        )

    def average_pnl(self) -> float:
        total = self.total_trades()
        if total == 0:
            return 0.0
        return round(self.net_pnl() / total, 2)

    def average_risk_reward(self) -> float:
        trades = self.closed_trades()

        if not trades:
            return 0.0

        return round(
            sum(trade.risk_reward_ratio for trade in trades) / len(trades),
            2,
        )

    def profit_factor(self) -> float:
        profit = self.total_profit()
        loss = abs(self.total_loss())

        if loss == 0:
            return 0.0

        return round(profit / loss, 2)

    def maximum_drawdown(self) -> float:
        equity = 0.0
        peak = 0.0
        max_drawdown = 0.0

        for trade in self.closed_trades():
            equity += trade.pnl

            if equity > peak:
                peak = equity

            drawdown = peak - equity

            if drawdown > max_drawdown:
                max_drawdown = drawdown

        return round(max_drawdown, 2)

    def summary(self) -> Dict:
        return {
            "total_trades": self.total_trades(),
            "winning_trades": self.winning_trades(),
            "losing_trades": self.losing_trades(),
            "breakeven_trades": self.breakeven_trades(),
            "win_rate": self.win_rate(),
            "total_profit": self.total_profit(),
            "total_loss": self.total_loss(),
            "net_pnl": self.net_pnl(),
            "average_pnl": self.average_pnl(),
            "average_risk_reward": self.average_risk_reward(),
            "profit_factor": self.profit_factor(),
            "maximum_drawdown": self.maximum_drawdown(),
        }

    def _setup_performance(self, attribute: str) -> Dict:
        groups: Dict[str, List[Trade]] = {}

        for trade in self.closed_trades():
            setup = getattr(trade, attribute, None)

            if setup:
                groups.setdefault(setup, []).append(trade)

        performance = {}

        for setup, trades in groups.items():
            wins = sum(1 for trade in trades if trade.result == "WIN")
            losses = sum(1 for trade in trades if trade.result == "LOSS")
            breakevens = sum(
                1 for trade in trades if trade.result == "BREAKEVEN"
            )

            total_pnl = round(
                sum(trade.pnl for trade in trades),
                2,
            )

            win_rate = round(
                (wins / len(trades)) * 100,
                2,
            ) if trades else 0.0

            performance[setup] = {
                "trades": len(trades),
                "wins": wins,
                "losses": losses,
                "breakevens": breakevens,
                "win_rate": win_rate,
                "net_pnl": total_pnl,
            }

        return performance

    def smc_performance(self) -> Dict:
        return self._setup_performance("smc_setup")

    def ict_performance(self) -> Dict:
        return self._setup_performance("ict_setup")

    def liquidity_performance(self) -> Dict:
        return self._setup_performance("liquidity_event")

    def strategy_performance(self) -> Dict:
        return {
            "smc": self.smc_performance(),
            "ict": self.ict_performance(),
            "liquidity": self.liquidity_performance(),
        }
