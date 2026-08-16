from dataclasses import dataclass
from typing import Optional

from app.analysis.structure.structure_types import (
    MarketBias,
    StructureEvent,
    StructureType,
)


@dataclass
class SMCContext:
    """Combined SMC/ICT market context."""

    structure_points: list[StructureType]
    structure_event: Optional[StructureEvent]
    structure_bias: MarketBias

    liquidity_bias: str
    liquidity_event: str

    combined_bias: MarketBias
    confidence: float

    explanation: str
