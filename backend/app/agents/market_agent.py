import pandas as pd

from app.services.forex_service import ForexService
from app.services.indicator_service import IndicatorService


class MarketAgent:
    def __init__(self):
        self.forex = ForexService()
        self.indicator = IndicatorService()

    def analyze(self, pair: str):

        df = self.forex.get_market_data(pair)

        # Flatten MultiIndex columns if present
        if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
            df.columns = df.columns.get_level_values(0)

        indicators = self.indicator.calculate(df)

        close = df["Close"]

        # Convert DataFrame column to Series if needed
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        latest_price = float(close.iloc[-1])

        return {
            "pair": pair,
            "price": round(latest_price, 5),
            "trend": indicators["trend"],
            "rsi": indicators["rsi"],
            "ema20": indicators["ema20"],
            "ema50": indicators["ema50"],
            "macd": indicators["macd"],
            "signal": indicators["signal"],
        }