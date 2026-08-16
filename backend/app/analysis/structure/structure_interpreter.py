from typing import Optional

from app.analysis.structure.structure_types import (
    MarketBias,
    StructureEvent,
    StructureType,
)


class StructureInterpreter:
    """Interpret market structure and generate a directional bias."""

    @staticmethod
    def interpret(
        structure_points: list[StructureType],
        event: Optional[StructureEvent] = None,
    ) -> MarketBias:
        if event == StructureEvent.CHANGE_OF_CHARACTER:
            if StructureType.HIGHER_HIGH in structure_points:
                return MarketBias.BEARISH

            if StructureType.LOWER_LOW in structure_points:
                return MarketBias.BULLISH

        bullish_points = {
            StructureType.HIGHER_HIGH,
            StructureType.HIGHER_LOW,
        }

        bearish_points = {
            StructureType.LOWER_HIGH,
            StructureType.LOWER_LOW,
        }

        bullish_score = len(
            set(structure_points) & bullish_points
        )

        bearish_score = len(
            set(structure_points) & bearish_points
        )

        if bullish_score > bearish_score:
            return MarketBias.BULLISH

        if bearish_score > bullish_score:
            return MarketBias.BEARISH

        return MarketBias.NEUTRAL
