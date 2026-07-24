from fastapi import APIRouter

from app.data.fetcher import get_forex_data
from app.analysis.indicators import calculate_indicators
from app.analysis.signals import generate_signal
from app.analysis.explanation import generate_explanation

router = APIRouter()


@router.get("/analyze")
def analyze(symbol: str = "EURUSD=X"):
    df = get_forex_data(symbol)
    df = calculate_indicators(df)

    result = generate_signal(df)

    result["symbol"] = symbol
    result["explanation"] = generate_explanation(result)

    return result