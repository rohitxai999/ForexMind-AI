from typing import Optional

from app.analysis.structure.structure_types import (
    MarketBias,
    StructureEvent,
)


class StructureEventDetector:
    """Detect BOS and CHOCH from price structure."""

    @staticmethod
    def detect_bos(
        current_price: float,
        previous_high: Optional[float],
        previous_low: Optional[float],
    ) -> Optional[StructureEvent]:
        if previous_high is not None and current_price > previous_high:
            return StructureEvent.BREAK_OF_STRUCTURE

        if previous_low is not None and current_price < previous_low:
            return StructureEvent.BREAK_OF_STRUCTURE

        return None

    @staticmethod
    def get_bos_bias(
        current_price: float,
        previous_high: Optional[float],
        previous_low: Optional[float],
    ) -> MarketBias:
        if previous_high is not None and current_price > previous_high:
            return MarketBias.BULLISH

        if previous_low is not None and current_price < previous_low:
            return MarketBias.BEARISH

        return MarketBias.NEUTRAL

    @staticmethod
    def detect_choch(
        current_price: float,
        current_bias: MarketBias,
        protected_high: Optional[float],
        protected_low: Optional[float],
    ) -> Optional[StructureEvent]:
        if current_bias == MarketBias.BULLISH:
            if protected_low is not None and current_price < protected_low:
                return StructureEvent.CHANGE_OF_CHARACTER

        if current_bias == MarketBias.BEARISH:
            if protected_high is not None and current_price > protected_high:
                return StructureEvent.CHANGE_OF_CHARACTER

        return None
