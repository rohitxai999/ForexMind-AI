from dataclasses import dataclass
from enum import Enum
from typing import Optional


class LiquidityType(str, Enum):
    BUY_SIDE = "buy_side"
    SELL_SIDE = "sell_side"


class LiquidityPoolType(str, Enum):
    SWING_HIGH = "swing_high"
    SWING_LOW = "swing_low"
    EQUAL_HIGH = "equal_high"
    EQUAL_LOW = "equal_low"


class SweepDirection(str, Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"


@dataclass
class LiquidityPool:
    price: float
    liquidity_type: LiquidityType
    pool_type: LiquidityPoolType
    index: int
    strength: float = 1.0


@dataclass
class LiquiditySweep:
    price: float
    liquidity_type: LiquidityType
    direction: SweepDirection
    index: int
    confirmation: bool = False
    swept_pool: Optional[LiquidityPool] = None


@dataclass
class LiquidityAnalysis:
    buy_side_liquidity: list[LiquidityPool]
    sell_side_liquidity: list[LiquidityPool]
    sweeps: list[LiquiditySweep]

    @property
    def total_liquidity_pools(self) -> int:
        return len(self.buy_side_liquidity) + len(self.sell_side_liquidity)

    @property
    def total_sweeps(self) -> int:
        return len(self.sweeps)
