from typing import List, Optional
from uuid import uuid4

from app.trading.models import Trade


class TradeManager:
    """
    Manages ForexMind AI trade records.

    This is the initial in-memory implementation.
    A persistent database layer can be added later.
    """

    def __init__(self):
        self._trades: List[Trade] = []

    def create_trade(self, trade: Trade) -> Trade:
        """
        Add a new trade to the trade history.
        """

        if trade.trade_id is None:
            trade.trade_id = str(uuid4())

        self._trades.append(trade)

        return trade

    def get_trade(self, trade_id: str) -> Optional[Trade]:
        """
        Retrieve a trade by its ID.
        """

        for trade in self._trades:
            if trade.trade_id == trade_id:
                return trade

        return None

    def close_trade(
        self,
        trade_id: str,
        result: str,
        pnl: float,
    ) -> Trade:
        """
        Close an existing trade.
        """

        trade = self.get_trade(trade_id)

        if trade is None:
            raise ValueError(f"Trade not found: {trade_id}")

        trade.close_trade(result, pnl)

        return trade

    def list_trades(self) -> List[Trade]:
        """
        Return all recorded trades.
        """

        return list(self._trades)

    def get_open_trades(self) -> List[Trade]:
        """
        Return trades that are still open.
        """

        return [
            trade
            for trade in self._trades
            if trade.result is None
        ]

    def get_closed_trades(self) -> List[Trade]:
        """
        Return completed trades.
        """

        return [
            trade
            for trade in self._trades
            if trade.result is not None
        ]

    def clear(self) -> None:
        """
        Clear all in-memory trade records.

        Useful for testing.
        """

        self._trades.clear()