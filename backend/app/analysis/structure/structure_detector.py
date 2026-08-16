from typing import Optional

from app.analysis.structure.structure_types import StructureType


class StructureDetector:
    """Detect market structure from swing highs and swing lows."""

    @staticmethod
    def classify_high(
        current_high: float,
        previous_high: Optional[float],
    ) -> Optional[StructureType]:
        if previous_high is None:
            return None

        if current_high > previous_high:
            return StructureType.HIGHER_HIGH

        return StructureType.LOWER_HIGH

    @staticmethod
    def classify_low(
        current_low: float,
        previous_low: Optional[float],
    ) -> Optional[StructureType]:
        if previous_low is None:
            return None

        if current_low > previous_low:
            return StructureType.HIGHER_LOW

        return StructureType.LOWER_LOW
