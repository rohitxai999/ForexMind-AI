from dataclasses import dataclass
from typing import Any, Optional

from app.analysis.structure.structure_types import (
    MarketBias,
    StructureEvent,
)


@dataclass
class OrderBlock:
    """Represents an SMC/ICT order block zone."""

    index: int
    direction: MarketBias
    high: float
    low: float
    open: float
    close: float
    strength: float = 1.0
    validated: bool = False
    mitigated: bool = False
    structure_event: Optional[StructureEvent] = None

    @property
    def midpoint(self) -> float:
        return (self.high + self.low) / 2

    @property
    def range(self) -> float:
        return self.high - self.low


class OrderBlockDetector:
    """
    Detect SMC/ICT-style order blocks from OHLC candles.

    A bullish order block is the final bearish candle before
    bullish displacement.

    A bearish order block is the final bullish candle before
    bearish displacement.
    """

    def __init__(
        self,
        lookback: int = 10,
        min_displacement_ratio: float = 1.0,
    ):
        if lookback < 1:
            raise ValueError("lookback must be at least 1")

        if min_displacement_ratio < 0:
            raise ValueError(
                "min_displacement_ratio cannot be negative"
            )

        self.lookback = lookback
        self.min_displacement_ratio = min_displacement_ratio

    def detect(
        self,
        candles: list[dict[str, Any]],
        event_index: int,
        direction: MarketBias,
        structure_event: Optional[StructureEvent] = None,
    ) -> Optional[OrderBlock]:
        self._validate_candles(candles)

        if not 0 <= event_index < len(candles):
            raise IndexError("event_index is outside candle range")

        if direction not in {
            MarketBias.BULLISH,
            MarketBias.BEARISH,
        }:
            return None

        if event_index == 0:
            return None

        start_index = max(0, event_index - self.lookback)

        displacement = self._displacement_size(
            candles[event_index]
        )

        for index in range(
            event_index - 1,
            start_index - 1,
            -1,
        ):
            candle = candles[index]

            if direction == MarketBias.BULLISH:
                is_opposing = candle["close"] < candle["open"]
            else:
                is_opposing = candle["close"] > candle["open"]

            if not is_opposing:
                continue

            order_block_range = candle["high"] - candle["low"]

            if order_block_range <= 0:
                continue

            strength = self._calculate_strength(
                displacement,
                order_block_range,
            )

            validated = (
                displacement
                >= order_block_range
                * self.min_displacement_ratio
            )

            return OrderBlock(
                index=index,
                direction=direction,
                high=candle["high"],
                low=candle["low"],
                open=candle["open"],
                close=candle["close"],
                strength=round(strength, 4),
                validated=validated,
                mitigated=self._is_mitigated(
                    candles,
                    index,
                    event_index,
                    direction,
                ),
                structure_event=structure_event,
            )

        return None

    def detect_all(
        self,
        candles: list[dict[str, Any]],
        direction: MarketBias,
    ) -> list[OrderBlock]:
        self._validate_candles(candles)

        if direction not in {
            MarketBias.BULLISH,
            MarketBias.BEARISH,
        }:
            return []

        order_blocks: list[OrderBlock] = []

        for index in range(1, len(candles)):
            previous = candles[index - 1]
            current = candles[index]

            if direction == MarketBias.BULLISH:
                displacement = current["close"] - current["open"]

                if displacement <= 0:
                    continue

                if previous["close"] >= previous["open"]:
                    continue

            else:
                displacement = current["open"] - current["close"]

                if displacement <= 0:
                    continue

                if previous["close"] <= previous["open"]:
                    continue

            order_block = self.detect(
                candles=candles,
                event_index=index,
                direction=direction,
            )

            if order_block is not None:
                order_blocks.append(order_block)

        return order_blocks

    def _displacement_size(
        self,
        candle: dict[str, Any],
    ) -> float:
        return abs(candle["close"] - candle["open"])

    def _calculate_strength(
        self,
        displacement: float,
        order_block_range: float,
    ) -> float:
        ratio = displacement / order_block_range
        return max(0.0, min(ratio, 5.0)) / 5.0

    def _is_mitigated(
        self,
        candles: list[dict[str, Any]],
        order_block_index: int,
        event_index: int,
        direction: MarketBias,
    ) -> bool:
        order_block = candles[order_block_index]

        for index in range(event_index + 1, len(candles)):
            candle = candles[index]

            if direction == MarketBias.BULLISH:
                if candle["low"] <= order_block["low"]:
                    return True

            elif direction == MarketBias.BEARISH:
                if candle["high"] >= order_block["high"]:
                    return True

        return False

    def _validate_candles(
        self,
        candles: list[dict[str, Any]],
    ) -> None:
        if not isinstance(candles, list):
            raise TypeError("candles must be a list")

        if not candles:
            raise ValueError("candles cannot be empty")

        required_fields = {
            "open",
            "high",
            "low",
            "close",
        }

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

            if not (
                candle["low"]
                <= candle["open"]
                <= candle["high"]
            ):
                raise ValueError(
                    f"candle at index {index} has invalid open"
                )

            if not (
                candle["low"]
                <= candle["close"]
                <= candle["high"]
            ):
                raise ValueError(
                    f"candle at index {index} has invalid close"
                )
