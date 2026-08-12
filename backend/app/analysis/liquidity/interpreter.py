from dataclasses import dataclass

from .models import (
    LiquidityAnalysis,
    LiquidityType,
    SweepDirection,
)


@dataclass
class LiquidityContext:
    bias: str
    event: str
    explanation: str
    confidence_contribution: float


class LiquidityInterpreter:
    """
    Converts raw liquidity detections into
    SMC/ICT-style market context.
    """

    def interpret(
        self,
        analysis: LiquidityAnalysis,
    ) -> LiquidityContext:

        if not analysis.sweeps:
            return LiquidityContext(
                bias="NEUTRAL",
                event="NO_LIQUIDITY_SWEEP",
                explanation=(
                    "No confirmed liquidity sweep was detected."
                ),
                confidence_contribution=0.0,
            )

        latest_sweep = max(
            analysis.sweeps,
            key=lambda sweep: sweep.index,
        )

        if latest_sweep.direction == SweepDirection.BEARISH:
            if latest_sweep.liquidity_type == LiquidityType.BUY_SIDE:
                return LiquidityContext(
                    bias="BEARISH",
                    event="BEARISH_BSL_SWEEP",
                    explanation=(
                        "Buy-side liquidity above a previous "
                        "liquidity pool was swept and price "
                        "closed back below the level."
                    ),
                    confidence_contribution=15.0,
                )

        if latest_sweep.direction == SweepDirection.BULLISH:
            if latest_sweep.liquidity_type == LiquidityType.SELL_SIDE:
                return LiquidityContext(
                    bias="BULLISH",
                    event="BULLISH_SSL_SWEEP",
                    explanation=(
                        "Sell-side liquidity below a previous "
                        "liquidity pool was swept and price "
                        "closed back above the level."
                    ),
                    confidence_contribution=15.0,
                )

        return LiquidityContext(
            bias="NEUTRAL",
            event="LIQUIDITY_EVENT",
            explanation=(
                "A liquidity event was detected but did not "
                "produce a directional SMC interpretation."
            ),
            confidence_contribution=0.0,
        )
