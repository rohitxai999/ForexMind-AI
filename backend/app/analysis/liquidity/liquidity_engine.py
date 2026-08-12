from typing import Any

from .models import (
    LiquidityAnalysis,
    LiquidityPool,
    LiquidityPoolType,
    LiquidityType,
    LiquiditySweep,
    SweepDirection,
)


class LiquidityEngine:
    """
    Detects SMC/ICT-style liquidity pools and liquidity sweeps
    from OHLC candle data.
    """

    def __init__(
        self,
        swing_lookback: int = 2,
        equal_tolerance: float = 0.0002,
    ):
        if swing_lookback < 1:
            raise ValueError("swing_lookback must be at least 1")

        if equal_tolerance < 0:
            raise ValueError("equal_tolerance cannot be negative")

        self.swing_lookback = swing_lookback
        self.equal_tolerance = equal_tolerance

    def analyze(self, candles: list[dict[str, Any]]) -> LiquidityAnalysis:
        self._validate_candles(candles)

        buy_side = self._detect_swing_highs(candles)
        sell_side = self._detect_swing_lows(candles)

        buy_side.extend(self._detect_equal_highs(candles))
        sell_side.extend(self._detect_equal_lows(candles))

        sweeps = self._detect_sweeps(
            candles,
            buy_side,
            sell_side,
        )

        return LiquidityAnalysis(
            buy_side_liquidity=buy_side,
            sell_side_liquidity=sell_side,
            sweeps=sweeps,
        )

    def _validate_candles(
        self,
        candles: list[dict[str, Any]],
    ) -> None:
        if not isinstance(candles, list):
            raise TypeError("candles must be a list")

        if not candles:
            raise ValueError("candles cannot be empty")

        required_fields = {"open", "high", "low", "close"}

        for index, candle in enumerate(candles):
            if not isinstance(candle, dict):
                raise TypeError(
                    f"candle at index {index} must be a dictionary"
                )

            missing = required_fields - candle.keys()

            if missing:
                raise ValueError(
                    f"candle at index {index} is missing: {missing}"
                )

            if candle["high"] < candle["low"]:
                raise ValueError(
                    f"candle at index {index} has high below low"
                )

    def _detect_swing_highs(
        self,
        candles: list[dict[str, Any]],
    ) -> list[LiquidityPool]:
        pools = []
        lookback = self.swing_lookback

        for index in range(
            lookback,
            len(candles) - lookback,
        ):
            current_high = candles[index]["high"]

            left_highs = [
                candles[i]["high"]
                for i in range(index - lookback, index)
            ]

            right_highs = [
                candles[i]["high"]
                for i in range(
                    index + 1,
                    index + lookback + 1,
                )
            ]

            if (
                all(current_high > value for value in left_highs)
                and all(current_high > value for value in right_highs)
            ):
                pools.append(
                    LiquidityPool(
                        price=current_high,
                        liquidity_type=LiquidityType.BUY_SIDE,
                        pool_type=LiquidityPoolType.SWING_HIGH,
                        index=index,
                        strength=1.0,
                    )
                )

        return pools

    def _detect_swing_lows(
        self,
        candles: list[dict[str, Any]],
    ) -> list[LiquidityPool]:
        pools = []
        lookback = self.swing_lookback

        for index in range(
            lookback,
            len(candles) - lookback,
        ):
            current_low = candles[index]["low"]

            left_lows = [
                candles[i]["low"]
                for i in range(index - lookback, index)
            ]

            right_lows = [
                candles[i]["low"]
                for i in range(
                    index + 1,
                    index + lookback + 1,
                )
            ]

            if (
                all(current_low < value for value in left_lows)
                and all(current_low < value for value in right_lows)
            ):
                pools.append(
                    LiquidityPool(
                        price=current_low,
                        liquidity_type=LiquidityType.SELL_SIDE,
                        pool_type=LiquidityPoolType.SWING_LOW,
                        index=index,
                        strength=1.0,
                    )
                )

        return pools

    def _detect_equal_highs(
        self,
        candles: list[dict[str, Any]],
    ) -> list[LiquidityPool]:
        pools = []

        for index in range(1, len(candles)):
            previous_high = candles[index - 1]["high"]
            current_high = candles[index]["high"]

            if self._approximately_equal(
                previous_high,
                current_high,
            ):
                pools.append(
                    LiquidityPool(
                        price=(previous_high + current_high) / 2,
                        liquidity_type=LiquidityType.BUY_SIDE,
                        pool_type=LiquidityPoolType.EQUAL_HIGH,
                        index=index,
                        strength=1.5,
                    )
                )

        return pools

    def _detect_equal_lows(
        self,
        candles: list[dict[str, Any]],
    ) -> list[LiquidityPool]:
        pools = []

        for index in range(1, len(candles)):
            previous_low = candles[index - 1]["low"]
            current_low = candles[index]["low"]

            if self._approximately_equal(
                previous_low,
                current_low,
            ):
                pools.append(
                    LiquidityPool(
                        price=(previous_low + current_low) / 2,
                        liquidity_type=LiquidityType.SELL_SIDE,
                        pool_type=LiquidityPoolType.EQUAL_LOW,
                        index=index,
                        strength=1.5,
                    )
                )

        return pools

    def _detect_sweeps(
        self,
        candles: list[dict[str, Any]],
        buy_side: list[LiquidityPool],
        sell_side: list[LiquidityPool],
    ) -> list[LiquiditySweep]:
        sweeps = []

        for index, candle in enumerate(candles):
            for pool in buy_side:
                if index <= pool.index:
                    continue

                if (
                    candle["high"] > pool.price
                    and candle["close"] < pool.price
                ):
                    sweeps.append(
                        LiquiditySweep(
                            price=pool.price,
                            liquidity_type=LiquidityType.BUY_SIDE,
                            direction=SweepDirection.BEARISH,
                            index=index,
                            confirmation=True,
                            swept_pool=pool,
                        )
                    )

            for pool in sell_side:
                if index <= pool.index:
                    continue

                if (
                    candle["low"] < pool.price
                    and candle["close"] > pool.price
                ):
                    sweeps.append(
                        LiquiditySweep(
                            price=pool.price,
                            liquidity_type=LiquidityType.SELL_SIDE,
                            direction=SweepDirection.BULLISH,
                            index=index,
                            confirmation=True,
                            swept_pool=pool,
                        )
                    )

        return sweeps

    def _approximately_equal(
        self,
        first: float,
        second: float,
    ) -> bool:
        difference = abs(first - second)
        return difference <= self.equal_tolerance
