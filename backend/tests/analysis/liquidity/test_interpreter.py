from app.analysis.liquidity.interpreter import LiquidityInterpreter
from app.analysis.liquidity.models import (
    LiquidityAnalysis,
    LiquidityPool,
    LiquidityPoolType,
    LiquiditySweep,
    LiquidityType,
    SweepDirection,
)


def test_bearish_bsl_sweep_interpretation():
    pool = LiquidityPool(
        price=112.0,
        liquidity_type=LiquidityType.BUY_SIDE,
        pool_type=LiquidityPoolType.SWING_HIGH,
        index=2,
    )

    sweep = LiquiditySweep(
        price=112.0,
        liquidity_type=LiquidityType.BUY_SIDE,
        direction=SweepDirection.BEARISH,
        index=4,
        confirmation=True,
        swept_pool=pool,
    )

    analysis = LiquidityAnalysis(
        buy_side_liquidity=[pool],
        sell_side_liquidity=[],
        sweeps=[sweep],
    )

    context = LiquidityInterpreter().interpret(analysis)

    assert context.bias == "BEARISH"
    assert context.event == "BEARISH_BSL_SWEEP"
    assert context.confidence_contribution == 15.0
    assert "Buy-side liquidity" in context.explanation


def test_bullish_ssl_sweep_interpretation():
    pool = LiquidityPool(
        price=90.0,
        liquidity_type=LiquidityType.SELL_SIDE,
        pool_type=LiquidityPoolType.SWING_LOW,
        index=1,
    )

    sweep = LiquiditySweep(
        price=90.0,
        liquidity_type=LiquidityType.SELL_SIDE,
        direction=SweepDirection.BULLISH,
        index=3,
        confirmation=True,
        swept_pool=pool,
    )

    analysis = LiquidityAnalysis(
        buy_side_liquidity=[],
        sell_side_liquidity=[pool],
        sweeps=[sweep],
    )

    context = LiquidityInterpreter().interpret(analysis)

    assert context.bias == "BULLISH"
    assert context.event == "BULLISH_SSL_SWEEP"
    assert context.confidence_contribution == 15.0
    assert "Sell-side liquidity" in context.explanation


def test_no_sweep_returns_neutral_context():
    analysis = LiquidityAnalysis(
        buy_side_liquidity=[],
        sell_side_liquidity=[],
        sweeps=[],
    )

    context = LiquidityInterpreter().interpret(analysis)

    assert context.bias == "NEUTRAL"
    assert context.event == "NO_LIQUIDITY_SWEEP"
    assert context.confidence_contribution == 0.0


def test_latest_sweep_is_used():
    bullish_sweep = LiquiditySweep(
        price=90.0,
        liquidity_type=LiquidityType.SELL_SIDE,
        direction=SweepDirection.BULLISH,
        index=3,
        confirmation=True,
    )

    bearish_sweep = LiquiditySweep(
        price=112.0,
        liquidity_type=LiquidityType.BUY_SIDE,
        direction=SweepDirection.BEARISH,
        index=5,
        confirmation=True,
    )

    analysis = LiquidityAnalysis(
        buy_side_liquidity=[],
        sell_side_liquidity=[],
        sweeps=[
            bullish_sweep,
            bearish_sweep,
        ],
    )

    context = LiquidityInterpreter().interpret(analysis)

    assert context.bias == "BEARISH"
    assert context.event == "BEARISH_BSL_SWEEP"
