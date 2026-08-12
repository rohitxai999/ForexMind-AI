from app.analysis.liquidity.liquidity_engine import LiquidityEngine
from app.analysis.liquidity.models import (
    LiquidityPoolType,
    LiquidityType,
    SweepDirection,
)


def test_detect_swing_high():
    candles = [
        {"open": 100, "high": 101, "low": 99, "close": 100},
        {"open": 100, "high": 102, "low": 99, "close": 101},
        {"open": 101, "high": 110, "low": 100, "close": 108},
        {"open": 108, "high": 103, "low": 101, "close": 102},
        {"open": 102, "high": 104, "low": 100, "close": 101},
    ]

    engine = LiquidityEngine(swing_lookback=1)
    result = engine.analyze(candles)

    swing_highs = [
        pool
        for pool in result.buy_side_liquidity
        if pool.pool_type == LiquidityPoolType.SWING_HIGH
    ]

    assert len(swing_highs) == 1
    assert swing_highs[0].price == 110
    assert swing_highs[0].liquidity_type == LiquidityType.BUY_SIDE


def test_detect_swing_low():
    candles = [
        {"open": 100, "high": 102, "low": 99, "close": 100},
        {"open": 100, "high": 103, "low": 98, "close": 99},
        {"open": 99, "high": 100, "low": 90, "close": 92},
        {"open": 92, "high": 95, "low": 94, "close": 94},
        {"open": 94, "high": 97, "low": 93, "close": 96},
    ]

    engine = LiquidityEngine(swing_lookback=1)
    result = engine.analyze(candles)

    swing_lows = [
        pool
        for pool in result.sell_side_liquidity
        if pool.pool_type == LiquidityPoolType.SWING_LOW
    ]

    assert len(swing_lows) == 1
    assert swing_lows[0].price == 90
    assert swing_lows[0].liquidity_type == LiquidityType.SELL_SIDE


def test_detect_equal_high():
    candles = [
        {"open": 100, "high": 105, "low": 99, "close": 103},
        {"open": 103, "high": 105.0001, "low": 100, "close": 104},
        {"open": 104, "high": 107, "low": 102, "close": 106},
    ]

    engine = LiquidityEngine(
        swing_lookback=1,
        equal_tolerance=0.001,
    )

    result = engine.analyze(candles)

    equal_highs = [
        pool
        for pool in result.buy_side_liquidity
        if pool.pool_type == LiquidityPoolType.EQUAL_HIGH
    ]

    assert len(equal_highs) == 1
    assert equal_highs[0].liquidity_type == LiquidityType.BUY_SIDE


def test_detect_equal_low():
    candles = [
        {"open": 100, "high": 102, "low": 95, "close": 99},
        {"open": 99, "high": 101, "low": 95.0001, "close": 100},
        {"open": 100, "high": 104, "low": 98, "close": 103},
    ]

    engine = LiquidityEngine(
        swing_lookback=1,
        equal_tolerance=0.001,
    )

    result = engine.analyze(candles)

    equal_lows = [
        pool
        for pool in result.sell_side_liquidity
        if pool.pool_type == LiquidityPoolType.EQUAL_LOW
    ]

    assert len(equal_lows) == 1
    assert equal_lows[0].liquidity_type == LiquidityType.SELL_SIDE


def test_detect_bearish_buy_side_sweep():
    candles = [
        {"open": 100, "high": 105, "low": 99, "close": 103},
        {"open": 103, "high": 110, "low": 101, "close": 108},
        {"open": 108, "high": 112, "low": 106, "close": 109},
        {"open": 109, "high": 108, "low": 104, "close": 106},
        {"open": 106, "high": 113, "low": 104, "close": 110},
    ]

    engine = LiquidityEngine(swing_lookback=1)
    result = engine.analyze(candles)

    bearish_sweeps = [
        sweep
        for sweep in result.sweeps
        if sweep.direction == SweepDirection.BEARISH
    ]

    assert len(bearish_sweeps) >= 1
    assert bearish_sweeps[0].liquidity_type == LiquidityType.BUY_SIDE
    assert bearish_sweeps[0].confirmation is True


def test_detect_bullish_sell_side_sweep():
    candles = [
        {"open": 100, "high": 103, "low": 95, "close": 98},
        {"open": 98, "high": 100, "low": 90, "close": 92},
        {"open": 92, "high": 96, "low": 91, "close": 94},
        {"open": 94, "high": 102, "low": 89, "close": 99},
    ]

    engine = LiquidityEngine(swing_lookback=1)
    result = engine.analyze(candles)

    bullish_sweeps = [
        sweep
        for sweep in result.sweeps
        if sweep.direction == SweepDirection.BULLISH
    ]

    assert len(bullish_sweeps) >= 1
    assert bullish_sweeps[0].liquidity_type == LiquidityType.SELL_SIDE
    assert bullish_sweeps[0].confirmation is True


def test_invalid_empty_candles():
    engine = LiquidityEngine()

    try:
        engine.analyze([])
        assert False
    except ValueError as error:
        assert str(error) == "candles cannot be empty"


def test_invalid_candle_fields():
    engine = LiquidityEngine()

    candles = [
        {
            "open": 100,
            "high": 105,
            "close": 103,
        }
    ]

    try:
        engine.analyze(candles)
        assert False
    except ValueError:
        assert True
