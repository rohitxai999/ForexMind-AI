from typing import Optional

from app.analysis.liquidity.interpreter import LiquidityContext
from app.analysis.structure.structure_interpreter import StructureInterpreter
from app.analysis.structure.structure_types import (
    MarketBias,
    StructureEvent,
    StructureType,
)

from .smc_context import SMCContext


class SMCEngine:
    """Combine liquidity and market structure into SMC context."""

    @staticmethod
    def combine(
        structure_points: list[StructureType],
        liquidity_context: LiquidityContext,
        structure_event: Optional[StructureEvent] = None,
    ) -> SMCContext:

        structure_bias = StructureInterpreter.interpret(
            structure_points,
            structure_event,
        )

        liquidity_bias = liquidity_context.bias.upper()

        if (
            structure_bias == MarketBias.BULLISH
            and liquidity_bias == "BULLISH"
        ):
            combined_bias = MarketBias.BULLISH
            confidence = 80.0

        elif (
            structure_bias == MarketBias.BEARISH
            and liquidity_bias == "BEARISH"
        ):
            combined_bias = MarketBias.BEARISH
            confidence = 80.0

        elif structure_bias != MarketBias.NEUTRAL:
            combined_bias = structure_bias
            confidence = 60.0

        elif liquidity_bias == "BULLISH":
            combined_bias = MarketBias.BULLISH
            confidence = 55.0

        elif liquidity_bias == "BEARISH":
            combined_bias = MarketBias.BEARISH
            confidence = 55.0

        else:
            combined_bias = MarketBias.NEUTRAL
            confidence = 0.0

        explanation = (
            f"Structure bias: {structure_bias.value}. "
            f"Liquidity bias: {liquidity_bias}. "
            f"Combined SMC bias: {combined_bias.value}."
        )

        return SMCContext(
            structure_points=structure_points,
            structure_event=structure_event,
            structure_bias=structure_bias,
            liquidity_bias=liquidity_context.bias,
            liquidity_event=liquidity_context.event,
            combined_bias=combined_bias,
            confidence=confidence,
            explanation=explanation,
        )
