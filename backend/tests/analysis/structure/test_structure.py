from app.analysis.structure.structure_detector import StructureDetector
from app.analysis.structure.structure_events import StructureEventDetector
from app.analysis.structure.structure_interpreter import StructureInterpreter
from app.analysis.structure.structure_types import (
    MarketBias,
    StructureEvent,
    StructureType,
)


def test_higher_high():
    result = StructureDetector.classify_high(1.1080, 1.1050)
    assert result == StructureType.HIGHER_HIGH


def test_lower_high():
    result = StructureDetector.classify_high(1.1030, 1.1050)
    assert result == StructureType.LOWER_HIGH


def test_higher_low():
    result = StructureDetector.classify_low(1.1020, 1.1000)
    assert result == StructureType.HIGHER_LOW


def test_lower_low():
    result = StructureDetector.classify_low(1.0980, 1.1000)
    assert result == StructureType.LOWER_LOW


def test_bullish_bos():
    result = StructureEventDetector.detect_bos(
        1.1080,
        1.1050,
        1.1000,
    )
    assert result == StructureEvent.BREAK_OF_STRUCTURE


def test_bearish_bos():
    result = StructureEventDetector.detect_bos(
        1.0970,
        1.1050,
        1.1000,
    )
    assert result == StructureEvent.BREAK_OF_STRUCTURE


def test_no_bos():
    result = StructureEventDetector.detect_bos(
        1.1020,
        1.1050,
        1.1000,
    )
    assert result is None


def test_bullish_choch():
    result = StructureEventDetector.detect_choch(
        1.0980,
        MarketBias.BULLISH,
        1.1050,
        1.1000,
    )
    assert result == StructureEvent.CHANGE_OF_CHARACTER


def test_bearish_choch():
    result = StructureEventDetector.detect_choch(
        1.1070,
        MarketBias.BEARISH,
        1.1050,
        1.1000,
    )
    assert result == StructureEvent.CHANGE_OF_CHARACTER


def test_bullish_structure_interpretation():
    result = StructureInterpreter.interpret(
        [
            StructureType.HIGHER_HIGH,
            StructureType.HIGHER_LOW,
        ]
    )
    assert result == MarketBias.BULLISH


def test_bearish_structure_interpretation():
    result = StructureInterpreter.interpret(
        [
            StructureType.LOWER_HIGH,
            StructureType.LOWER_LOW,
        ]
    )
    assert result == MarketBias.BEARISH


def test_neutral_structure_interpretation():
    result = StructureInterpreter.interpret([])
    assert result == MarketBias.NEUTRAL
