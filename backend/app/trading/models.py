from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Trade:
    """
    Represents a ForexMind AI trade.

    The model is designed around the project's
    SMC + ICT + Liquidity analysis architecture.
    """

    pair: str
    direction: str

    entry_price: float
    stop_loss: float
    take_profit: float

    position_size: float
    risk_percent: float

    smc_setup: Optional[str] = None
    ict_setup: Optional[str] = None
    liquidity_event: Optional[str] = None

    confidence: Optional[float] = None

    result: Optional[str] = None
    pnl: float = 0.0

    trade_id: Optional[str] = None

    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        self.direction = self.direction.upper()

        if self.direction not in {"BUY", "SELL"}:
            raise ValueError("direction must be BUY or SELL")

        if self.entry_price <= 0:
            raise ValueError("entry_price must be greater than 0")

        if self.stop_loss <= 0:
            raise ValueError("stop_loss must be greater than 0")

        if self.take_profit <= 0:
            raise ValueError("take_profit must be greater than 0")

        if self.position_size <= 0:
            raise ValueError("position_size must be greater than 0")

        if self.risk_percent < 0:
            raise ValueError("risk_percent cannot be negative")

        if self.confidence is not None:
            if not 0 <= self.confidence <= 100:
                raise ValueError("confidence must be between 0 and 100")

    @property
    def risk_reward_ratio(self) -> float:
        """
        Calculate the planned Risk/Reward ratio.
        """

        risk = abs(self.entry_price - self.stop_loss)
        reward = abs(self.take_profit - self.entry_price)

        if risk == 0:
            return 0.0

        return round(reward / risk, 2)

    def close_trade(self, result: str, pnl: float) -> None:
        """
        Close the trade and record its result.
        """

        result = result.upper()

        if result not in {"WIN", "LOSS", "BREAKEVEN"}:
            raise ValueError(
                "result must be WIN, LOSS, or BREAKEVEN"
            )

        self.result = result
        self.pnl = float(pnl)