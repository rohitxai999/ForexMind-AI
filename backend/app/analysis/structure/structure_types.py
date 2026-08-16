from enum import Enum


class StructureType(str, Enum):
    HIGHER_HIGH = "HH"
    HIGHER_LOW = "HL"
    LOWER_HIGH = "LH"
    LOWER_LOW = "LL"


class StructureEvent(str, Enum):
    BREAK_OF_STRUCTURE = "BOS"
    CHANGE_OF_CHARACTER = "CHOCH"


class MarketBias(str, Enum):
    BULLISH = "bullish"
    BEARISH = "bearish"
    NEUTRAL = "neutral"
