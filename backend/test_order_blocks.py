from app.analysis.smc.order_blocks import OrderBlockDetector
from app.analysis.structure.structure_types import (
    MarketBias,
    StructureEvent,
)


def test_detect_bullish_order_block():
    candles = [
        {"open": 100, "high": 103, "low": 99, "close": 101},
        {"open": 102, "high": 103, "low": 98, "close": 99},
        {"open": 99, "high": 108, "low": 98, "close": 107},
    ]

    detector = OrderBlockDetector()

    result = detector.detect(
        candles,
        event_index=2,
        direction=MarketBias.BULLISH,
        structure_event=StructureEvent.BREAK_OF_STRUCTURE,
    )

    assert result is not None
    assert result.index == 1
    assert result.direction == MarketBias.BULLISH
    assert result.high == 103
    assert result.low == 98
    assert result.validated is True
    assert result.structure_event == StructureEvent.BREAK_OF_STRUCTURE


def test_detect_bearish_order_block():
    candles = [
        {"open": 100, "high": 103, "low": 99, "close": 101},
        {"open": 99, "high": 104, "low": 98, "close": 103},
        {"open": 102, "high": 103, "low": 94, "close": 95},
    ]

    detector = OrderBlockDetector()

    result = detector.detect(
        candles,
        event_index=2,
        direction=MarketBias.BEARISH,
        structure_event=StructureEvent.BREAK_OF_STRUCTURE,
    )

    assert result is not None
    assert result.index == 1
    assert result.direction == MarketBias.BEARISH
    assert result.high == 104
    assert result.low == 98
    assert result.validated is True


def test_no_order_block_when_no_opposing_candle():
    candles = [
        {"open": 100, "high": 103, "low": 99, "close": 102},
        {"open": 102, "high": 106, "low": 101, "close": 105},
        {"open": 105, "high": 110, "low": 104, "close": 109},
    ]

    detector = OrderBlockDetector()

    result = detector.detect(
        candles,
        event_index=2,
        direction=MarketBias.BULLISH,
    )

    assert result is None


def test_order_block_strength_is_bounded():
    candles = [
        {"open": 100, "high": 103, "low": 99, "close": 101},
        {"open": 102, "high": 103, "low": 98, "close": 99},
        {"open": 99, "high": 120, "low": 98, "close": 119},
    ]

    detector = OrderBlockDetector()

    result = detector.detect(
        candles,
        event_index=2,
        direction=MarketBias.BULLISH,
    )

    assert result is not None
    assert 0.0 <= result.strength <= 1.0


def test_bullish_order_block_mitigation():
    candles = [
        {"open": 100, "high": 103, "low": 99, "close": 101},
        {"open": 102, "high": 103, "low": 98, "close": 99},
        {"open": 99, "high": 108, "low": 98, "close": 107},
        {"open": 107, "high": 109, "low": 97, "close": 105},
    ]

    detector = OrderBlockDetector()

    result = detector.detect(
        candles,
        event_index=2,
        direction=MarketBias.BULLISH,
    )

    assert result is not None
    assert result.mitigated is True


def test_invalid_event_index():
    candles = [
        {"open": 100, "high": 103, "low": 99, "close": 101},
    ]

    detector = OrderBlockDetector()

    try:
        detector.detect(
            candles,
            event_index=5,
            direction=MarketBias.BULLISH,
        )
        assert False
    except IndexError:
        assert True


def test_invalid_candle_is_rejected():
    candles = [
        {
            "open": 100,
            "high": 90,
            "low": 95,
            "close": 98,
        }
    ]

    detector = OrderBlockDetector()

    try:
        detector.detect(
            candles,
            event_index=0,
            direction=MarketBias.BULLISH,
        )
        assert False
    except ValueError:
        assert True
