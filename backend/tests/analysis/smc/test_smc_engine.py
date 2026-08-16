from app.analysis.liquidity.interpreter import LiquidityContext
from app.analysis.smc.smc_engine import SMCEngine
from app.analysis.structure.structure_types import (
    MarketBias,
    StructureType,
)


def test_bullish_structure_and_liquidity():
    liquidity = LiquidityContext(
        bias="BULLISH",
        event="BULLISH_SSL_SWEEP",
        explanation="Sell-side liquidity swept.",
        confidence_contribution=15.0,
    )

    result = SMCEngine.combine(
        [
            StructureType.HIGHER_HIGH,
            StructureType.HIGHER_LOW,
        ],
        liquidity,
    )

    assert result.structure_bias == MarketBias.BULLISH
    assert result.liquidity_bias == "BULLISH"
    assert result.combined_bias == MarketBias.BULLISH
    assert result.confidence == 80.0


def test_bearish_structure_and_liquidity():
    liquidity = LiquidityContext(
        bias="BEARISH",
        event="BEARISH_BSL_SWEEP",
        explanation="Buy-side liquidity swept.",
        confidence_contribution=15.0,
    )

    result = SMCEngine.combine(
        [
            StructureType.LOWER_HIGH,
            StructureType.LOWER_LOW,
        ],
        liquidity,
    )

    assert result.structure_bias == MarketBias.BEARISH
    assert result.liquidity_bias == "BEARISH"
    assert result.combined_bias == MarketBias.BEARISH
    assert result.confidence == 80.0


def test_structure_only_bias():
    liquidity = LiquidityContext(
        bias="NEUTRAL",
        event="NO_LIQUIDITY_SWEEP",
        explanation="No sweep detected.",
        confidence_contribution=0.0,
    )

    result = SMCEngine.combine(
        [
            StructureType.HIGHER_HIGH,
            StructureType.HIGHER_LOW,
        ],
        liquidity,
    )

    assert result.combined_bias == MarketBias.BULLISH
    assert result.confidence == 60.0


def test_liquidity_only_bias():
    liquidity = LiquidityContext(
        bias="BULLISH",
        event="BULLISH_SSL_SWEEP",
        explanation="Sell-side liquidity swept.",
        confidence_contribution=15.0,
    )

    result = SMCEngine.combine(
        [],
        liquidity,
    )

    assert result.combined_bias == MarketBias.BULLISH
    assert result.confidence == 55.0


def test_neutral_smc_context():
    liquidity = LiquidityContext(
        bias="NEUTRAL",
        event="NO_LIQUIDITY_SWEEP",
        explanation="No sweep detected.",
        confidence_contribution=0.0,
    )

    result = SMCEngine.combine([], liquidity)

    assert result.combined_bias == MarketBias.NEUTRAL
    assert result.confidence == 0.0
